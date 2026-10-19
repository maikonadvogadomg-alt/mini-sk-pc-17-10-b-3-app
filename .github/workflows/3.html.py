    const fs = require('fs');
    const path = require('path');

    function juntarProjeto(pasta) {
        const pastaAbsoluta = path.resolve(pasta);
        const indexPath = path.join(pastaAbsoluta, 'index.html');

        if (!fs.existsSync(indexPath)) {
            console.error('❌ Não achei o index.html dentro de: ' + pasta);
            process.exit(1);
        }

        let html = fs.readFileSync(indexPath, 'utf8');
        const usados = [];
        const faltando = [];

        function ler(rel) {
            if (rel.startsWith('http:') || rel.startsWith('https:') || rel.startsWith('data:')) return null;
            const caminho = path.normalize(path.join(pastaAbsoluta, rel.split('?')[0].split('#')[0]));
            if (!caminho.startsWith(pastaAbsoluta) || !fs.existsSync(caminho)) {
                faltando.push(rel);
                return null;
            }
            usados.push(rel);
            return caminho;
        }

        // Lógica para CSS
        html = html.replace(/<link\b[^>]*rel\s*=\s*["']?stylesheet[^>]*>/gi, (match) => {
            const hrefMatch = match.match(/href\s*=\s*["']([^"']+)/i);
            const href = hrefMatch && hrefMatch[1];
            const caminhoArquivo = href && ler(href);
            if (!caminhoArquivo) return match;
            const conteudoCss = fs.readFileSync(caminhoArquivo, 'utf8');
            return `<style>/* ${href} */\n${conteudoCss}\n</style>`;
        });

        // ... (continuaria com a lógica para JS e imagens, similar ao juntar.py) ...

        const saida = `${pastaAbsoluta}-UNICO.html`;
        fs.writeFileSync(saida, html, 'utf8');
        console.log('✅ Pronto:', saida);
        console.log('   Peças colocadas dentro:', usados.length);
        if (faltando.length > 0) {
            console.log('⚠️  Não achei estas peças (ficaram como estavam):');
            faltando.forEach(f => console.log('    -', f));
        }
    }

    if (require.main === module) {
        if (process.argv.length < 3) {
            console.log(`
JUNTAR — transforma um projeto "em pedaços" (index.html + pasta css + pasta js)
num ARQUIVO HTML ÚNICO, que abre sozinho em qualquer lugar.

Como usar (no computador ou no Termux):
    node juntar.js  PASTA-DO-PROJETO
Exemplo:
    node juntar.js  Laboratorio
Sai o arquivo  Laboratorio-UNICO.html  ao lado da pasta. A pasta original não muda.
            `);
            process.exit(1);
        }
        juntarProjeto(process.argv[2]);
    }
    