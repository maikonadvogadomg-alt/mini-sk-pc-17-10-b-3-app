# -*- coding: utf-8 -*-
"""
JUNTAR — transforma um projeto "em pedaços" (index.html + pasta css + pasta js + HTML modulares)
num ARQUIVO HTML ÚNICO, que abre sozinho em qualquer lugar.

Como usar (no computador ou no Termux):
    python juntar.py  PASTA-DO-PROJETO
Exemplo:
    python juntar.py  Laboratorio
Sai o arquivo  Laboratorio-UNICO.html  ao lado da pasta. A pasta original não muda.

Para incluir pedaços de HTML (modular):
No seu index.html (ou outro HTML), use:
    <!-- INCLUIR: components/cabecalho.html -->
    <!-- INCLUIR: paginas/minha-secao.html -->
O script vai ler o arquivo e colocar o conteúdo dele no lugar do comentário.
"""
import os, re, sys, base64, mimetypes

def juntar(pasta):
    pasta = os.path.abspath(pasta)
    index = os.path.join(pasta, 'index.html')
    if not os.path.isfile(index):
        sys.exit('❌ Não achei o index.html dentro de: ' + pasta)
    html = open(index, encoding='utf-8').read()
    usados, faltando = [], []

    def ler(rel):
        # Se for um link da internet ou dados base64, não tenta ler localmente
        if re.match(r'^(https?:)?//', rel) or rel.startswith('data:'): return None
        # Normaliza o caminho para garantir que seja seguro e dentro da pasta do projeto
        caminho = os.path.normpath(os.path.join(pasta, rel.split('?')[0].split('#')[0]))
        if not caminho.startswith(pasta) or not os.path.isfile(caminho):
            faltando.append(rel); return None
        usados.append(rel); return caminho

    # 1) cada  <link rel="stylesheet" href="css/x.css">  vira  <style> (o conteúdo) </style>
    def css(m):
        href = re.search(r'href\s*=\s*["\']([^"\']+)', m.group(0))
        c = href and ler(href.group(1))
        if not c: return m.group(0)
        return '<style>/* ' + href.group(1) + ' */\n' + open(c, encoding='utf-8').read() + '\n</style>'
    html = re.sub(r'<link\b[^>]*rel\s*=\s*["\']?stylesheet[^>]*>', css, html, flags=re.I)

    # 2) cada  <script src="js/x.js"></script>  vira  <script> (o conteúdo) </script>
    def js(m):
        abre = m.group(1)
        src = re.search(r'\bsrc\s*=\s*["\']([^"\']+)', abre)
        c = src and ler(src.group(1))
        if not c: return m.group(0)
        resto = re.sub(r'\s*\bsrc\s*=\s*["\'][^"\']+["\']', '', abre)
        codigo = open(c, encoding='utf-8').read().replace('</script', '<\\/script') # Evita fechar a tag script prematuramente
        return resto + '\n/* ' + src.group(1) + ' */\n' + codigo + '\n</script>'
    html = re.sub(r'(<script\b[^>]*\bsrc\s*=[^>]*>)\s*</script>', js, html, flags=re.I)

    # 3) ícones e imagens pequenas (até 300 KB) vão para dentro também
    def img(m):
        rel = m.group(2)
        # Se já é data:URI ou não é um caminho local para ler
        c = ler(rel) if not rel.startswith('data:') else None
        # Se não achou o arquivo ou ele é muito grande, deixa como está
        if not c or os.path.getsize(c) > 300 * 1024: return m.group(0)
        tipo = mimetypes.guess_type(c)[0] or 'application/octet-stream' # Tenta adivinhar o tipo do arquivo
        # Retorna a tag com a imagem em base64
        return m.group(1) + 'data:' + tipo + ';base64,' + base64.b64encode(open(c, 'rb').read()).decode() + m.group(3)
    html = re.sub(r'(<(?:img|link)\b[^>]*?(?:src|href)\s*=\s*["\'])((?:icons|img|imagens|assets)/[^"\']+)(["\'])', img, html, flags=re.I)

    # 4) cada <!-- INCLUIR: caminho/do/arquivo.html --> vira o conteúdo do arquivo
    def incluir_html(m):
        rel = m.group(1).strip() # Pega o caminho do arquivo (ex: components/cabecalho.html)
        c = ler(rel) # Usa a função 'ler' existente para encontrar o arquivo
        if not c: return m.group(0) # Se não achou, deixa o marcador como está
        return open(c, encoding='utf-8').read() # Retorna o conteúdo do arquivo HTML
    # Aplica a substituição depois de CSS, JS e Imagens
    html = re.sub(r'<!--\s*INCLUIR:\s*([^>]+?)\s*-->', incluir_html, html, flags=re.I)


    saida = pasta.rstrip(os.sep) + '-UNICO.html'
    open(saida, 'w', encoding='utf-8').write(html)
    print('✅ Pronto:', saida)
    print('   Peças colocadas dentro:', len(usados))
    if faltando:
        print('⚠️  Não achei estas peças (ficaram como estavam):')
        for f in faltando: print('    -', f)

if __name__ == '__main__':
    if len(sys.argv) < 2: sys.exit(__doc__)
    juntar(sys.argv[1])
