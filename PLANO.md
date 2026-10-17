# 📋 Plano do projeto: Mini-SK-PC-17-10-b (3)

_Gerado em 17/10/2026, 11:28:34 — sem IA, lendo os arquivos._

## 📊 Visão geral
| Item | Valor |
|---|---|
| Arquivos | 55 |
| Linhas | 11.470 |
| Telas/páginas | 1 |
| Rotas do backend | 0 |
| Chamadas do app | 0 |
| Tabelas do banco | 0 |
| Variáveis de ambiente | 8 |

**Linguagens:** JavaScript (45), Imagem (2), Markdown (2), JSON (2), YAML (1), Outros (1), CSS (1), HTML (1)

## 💡 O que fazer (em ordem)
1. 🧹 Tirar a Replit de 13 arquivo(s) (🏗️ Preparar → Fazer tudo)
2. 🔐 Criar um .env.example com: BASE_PATH, DADOS_EM, GITHUB_STEP_SUMMARY, LOCALAPPDATA, PONTE_BASE, PONTE_CODIGO, PONTE_PORTA, TESTE_SAIR (os valores você coloca no servidor, nunca no código)
3. 📝 Criar um README.md explicando como rodar

## 🚀 Por onde começa
- `app/index.html`

## ⌨️ Comandos (package.json)
| Pasta | Comando | O que roda |
|---|---|---|
| . | `npm run programa` | `electron .` |
| . | `npm run exe` | `electron-builder --win nsis portable --x64 --publish never` |

## 📱 Telas e páginas
| Endereço | Arquivo |
|---|---|
| `app/index.html` | app/index.html |

## 🖥️ Rotas do backend
_Nenhum encontrado._

## 📡 O que o app pede ao servidor
_Nenhum encontrado._

## 🔌 O que falta no backend
✅ Tudo que o app chama tem rota no projeto (ou o app não usa servidor).

## 🗄️ Banco de dados
_Nenhuma tabela encontrada._

## 🔐 Variáveis de ambiente (configurar no servidor)
- `BASE_PATH`
- `DADOS_EM`
- `GITHUB_STEP_SUMMARY`
- `LOCALAPPDATA`
- `PONTE_BASE`
- `PONTE_CODIGO`
- `PONTE_PORTA`
- `TESTE_SAIR`

_Só os nomes. Os valores (chaves, senhas) nunca vão no código nem no GitHub._

## 🤖 IA usada
- api.groq.com
- console.groq.com
- generativelanguage.googleapis.com
- openrouter.ai
- api.anthropic.com
- console.anthropic.com
- api.openai.com
- platform.openai.com

## 🌐 Serviços de fora que ele acessa
- aistudio.google.com
- api.anthropic.com
- api.exemplo.com
- api.expo.dev
- api.github.com
- api.groq.com
- api.npms.io
- api.openai.com
- api.perplexity.ai
- api.x.ai
- appassets.androidplatform.net
- cdn.jsdelivr.net
- cdn.tailwindcss.com
- console.anthropic.com
- console.groq.com
- console.x.ai
- esm.sh
- expo.dev
- generativelanguage.googleapis.com
- github.com
- mail.google.com
- ollama.com
- openapi.monica.im
- openrouter.ai
- platform.monica.im
- platform.openai.com
- registry.npmjs.org
- seu-usuario.github.io
- u.expo.dev
- unpkg.com
- www.google.com
- www.npmjs.com
- www.perplexity.ai
- xxxx.supabase.co

## 📦 Peças principais (dependências)
`ws`

## 🧹 Arquivos com coisa da Replit
- app/js/70-search.js
- app/js/80-ai.js
- app/js/86-terminal.js
- app/js/86c-termux.js
- app/js/88-inventario.js
- app/js/90-github.js
- app/js/95-pwa.js
- app/js/96b-eas.js
- app/js/96c-preparar.js
- app/js/97-analise.js
- app/js/lib/expo-core.js
- app/js/lib/plano-core.js
- app/js/lib/receita-core.js

## 🔁 Roteiro para recriar fora da Replit
1. Importar o projeto no Mini SK e tocar em 🏗️ Preparar → ✅ Fazer tudo (tira a Replit, cria os arquivos que faltam).
2. Não tem backend: o site sozinho basta (Netlify ou GitHub Pages).
3. Variáveis: cadastrar 8 variável(is) no servidor (lista acima).
4. Testar a prévia; se der erro, 🤖 Mandar os erros para a IA.
5. App: 📲 Instalável (PWA), 📦 APK ou 🖥️ Desktop (.exe) pelo 🏗️ Preparar.

## 🌳 Árvore de arquivos
```
├─ 📁 .github/
│  └─ 📁 workflows/
│     └─ programa-exe.yml
├─ 📁 app/
│  ├─ 📁 css/
│  │  └─ app.css
│  ├─ 📁 icons/
│  │  ├─ icon-192.png
│  │  └─ icon-512.png
│  ├─ 📁 js/
│  │  ├─ 📁 lib/
│  │  │  ├─ expo-core.js
│  │  │  ├─ nacl-fast.min.js
│  │  │  ├─ plano-core.js
│  │  │  ├─ receita-core.js
│  │  │  └─ selar.js
│  │  ├─ 00-core.js
│  │  ├─ 04-conta.js
│  │  ├─ 10-fs.js
│  │  ├─ 20-zip.js
│  │  ├─ 30-highlight.js
│  │  ├─ 40-editor.js
│  │  ├─ 50-tree.js
│  │  ├─ 60-preview.js
│  │  ├─ 61-tsx.js
│  │  ├─ 70-search.js
│  │  ├─ 80-ai.js
│  │  ├─ 81-gasto.js
│  │  ├─ 83-voz.js
│  │  ├─ 84-ponte.js
│  │  ├─ 85-checkpoints.js
│  │  ├─ 86-terminal.js
│  │  ├─ 86b-node.js
│  │  ├─ 86c-termux.js
│  │  ├─ 86e-atalhos.js
│  │  ├─ 86f-pasta-viva.js
│  │  ├─ 87-links.js
│  │  ├─ 88-inventario.js
│  │  ├─ 89-config.js
│  │  ├─ 90-github.js
│  │  ├─ 91-acoes.js
│  │  ├─ 92-playground.js
│  │  ├─ 93-conversa.js
│  │  ├─ 94-fatiador.js
│  │  ├─ 95-pwa.js
│  │  ├─ 96-apk.js
│  │  ├─ 96b-eas.js
│  │  ├─ 96c-preparar.js
│  │  ├─ 97-analise.js
│  │  ├─ 98-api.js
│  │  └─ 99-app.js
│  ├─ index.html
│  ├─ LEIA-ME.md
│  ├─ manifest.json
│  └─ sw.js
├─ 📁 electron/
│  ├─ main.cjs
│  ├─ ponte.cjs
│  ├─ preload.cjs
│  └─ terminal.cjs
├─ .gitignore
├─ LEIA-ME.md
└─ package.json
```
