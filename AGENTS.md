# Instruções para o site GABiSOU

## Objetivo e referências
- Site institucional para explicar a oferta, transmitir confiança em quem executa e iniciar uma conversa comercial.
- O redesign aprovado de Carol Faustino no Figma é a referência visual; a prévia V3 é somente contexto e base técnica. Arquivo, frame da primeira entrega e extração atual estão em `docs/DESIGN-HERO.md`.
- Repositório e convenções existentes orientam a implementação. Leia o estado atual no início de `docs/CONTINUIDADE.md`; seus registros históricos não comprovam aprovação do redesign.
- Não inventar clientes, resultados, depoimentos, experiência, contatos ou fotos; não expor urgência comercial.

## Base e comandos
- HTML/CSS estáticos. Fontes editáveis: `dist/index.html`, `dist/styles.css`, `dist/assets/`. Aqui `dist/` é a fonte versionada, não uma pasta descartável.
- Sem framework, package.json, gerenciador de pacotes ou lockfile. Python 3 usa apenas a biblioteca padrão para verificar, servir e preparar release.
- Conferir: `python scripts/check.py`.
- Servir localmente: `python -m http.server 8000 --bind 127.0.0.1 --directory dist`.
- Preparar release somente com origem confirmada: `python scripts/prepare_release.py --origin <ORIGEM_HTTPS_CONFIRMADA> --output build`; verificar com `python scripts/check.py build --public`. Gerar arquivos não publica.
- No Windows, identificar o Python já disponível; não instalar ou trocar ferramentas automaticamente. `py -3` pode substituir `python` se o launcher estiver confirmado.

## Execução
- Confirmar branch, commit e alterações existentes antes de editar e antes do handoff. Usar branch delimitada; não descartar alterações nem editar em paralelo os mesmos arquivos.
- Clientes sem leitura automática de AGENTS.md devem lê-lo explicitamente. A presença de um plugin não comprova permissão, terminal ou navegador.
- Aproveitar a stack existente. JavaScript mínimo somente quando necessário ao comportamento aprovado; não introduzir framework, backend, CMS ou dependências sem necessidade demonstrada.
- Primeiro obter contexto e imagem do cabeçalho/abertura aprovado; implementar e conferir desktop/mobile antes das demais seções.
- Registrar links/IDs, tipografia, cores, espaçamentos, assets e decisões responsivas na seção de design de CONTINUIDADE.md. Distinguir informação explícita e inferência; reutilizar extrações.
- Baixar assets/fontes autorizados para o projeto; não depender de URLs temporárias ou localhost em produção.
- Sem compra, nova assinatura, merge, deploy ou alteração de DNS nesta etapa. Não enviar mensagens a terceiros.
- Reaproveitar CONTINUIDADE.md e VERIFICACAO.md; manter registros curtos e vinculados ao commit verificado.

## Conclusão e evidências
- Executar checks pertinentes; comparar a renderização com o frame Figma nas mesmas dimensões e conferir mobile.
- Conferir assets/fontes, links/menu/CTA, teclado/foco/rótulos, console e ausência de transbordamento horizontal.
- Captura da própria versão anterior serve para regressão, não para comprovar fidelidade ao Figma.
- Devolver branch/commit ou patch, comandos e resultados, capturas/preview, limitações e próximo passo. Não declarar pronto/testado sem a evidência correspondente.
