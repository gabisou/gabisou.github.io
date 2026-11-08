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
- Produção: branch `main` do repositório `gabisou/gabisou.github.io`, projeto Netlify existente `gabisou-landing-page`, domínio `https://gabisou.com`. Alterações em branches de tarefa; integrar por PR após checks e revisão da etapa. O deploy automático deve acompanhar merges/pushes na `main`; não selecionar `codex/figma-redesign` como branch de produção. Confirmar o vínculo e o deploy real no checkpoint antes de afirmar publicação.
- Confirmar branch, commit e alterações existentes antes de editar e antes do handoff. Usar branch delimitada; não descartar alterações nem editar em paralelo os mesmos arquivos.
- Clientes sem leitura automática de AGENTS.md devem lê-lo explicitamente. A presença de um plugin não comprova permissão, terminal ou navegador.
- Aproveitar a stack existente. JavaScript mínimo somente quando necessário ao comportamento aprovado; não introduzir framework, backend, CMS ou dependências sem necessidade demonstrada.
- Seguir a etapa atribuída em `docs/ARQUITETURA-E-ETAPAS.md`. Header e hero são entregas separadas: header primeiro, com desktop/mobile e verificação visual. Não executar o antigo handoff que reunia ambos.
- A arquitetura recomendada é HTML/CSS com JS nativo quando necessário. Preservar componentes fora do escopo ao introduzir tokens e fontes; evoluir checks legados apenas quando houver requisito real.
- Registrar links/IDs, tipografia, cores, espaçamentos, assets e decisões responsivas na seção de design de CONTINUIDADE.md. Distinguir informação explícita e inferência; reutilizar extrações.
- Baixar assets/fontes autorizados para o projeto; não depender de URLs temporárias ou localhost em produção.
- Sem compra, nova assinatura, merge, deploy ou alteração de DNS nesta etapa. Não enviar mensagens a terceiros.
- Reaproveitar CONTINUIDADE.md e VERIFICACAO.md; manter registros curtos e vinculados ao commit verificado.

## Filosofia de layout — diretriz de Gabriel
- Aplicar ao propor, implementar e revisar: container → regiões → grupos/componentes → conteúdo. Grid é a primeira opção estrutural; Flexbox organiza grupos lineares quando apropriado. Os filhos se adaptam ao espaço organizado pelo pai.
- Ler a diretriz completa em `docs/ARQUITETURA-E-ETAPAS.md`, seção “Filosofia de layout adotada”. Ela define largura e altura, limites, proporções, falta de espaço e evidências; não substitui o Figma aprovado.
- Preferir relações, conteúdo e limites a dimensões rígidas de captura. Nesta página, altura acompanha conteúdo; não forçar seções a caber numa tela. Preservar proporção dos assets, legibilidade e áreas de interação.
- Cada proposta/retorno deve explicar quem organiza cada região, como os dois eixos são determinados, o que cresce/encolhe e como o layout se reorganiza. Inspecionar padrões existentes antes de alterar.
- Validar larguras e alturas distintas, redimensionamento contínuo, conteúdo real/textos longos, ampliação de texto, zoom e teclado. Não ocultar conteúdo essencial nem encolher controles/texto indefinidamente para evitar overflow. Informar verificações pendentes.
- Em dúvida sobre sintaxe, suporte ou comportamento, consultar documentação oficial atual e citar a fonte consultada. Não impor uso de todas as funções CSS ou uma biblioteca nova.

## Capacidade e custo
- Seguir “Capacidade, custo e transição entre modos” em `docs/ARQUITETURA-E-ETAPAS.md`: maior capacidade/máximo para fechar decisões difíceis e contratos executáveis; econômico/esforço suficiente para implementações pequenas, checks e ajustes.
- Reaproveitar decisões e contexto já preparados. O contrato do header já existe: não refazer planejamento em máximo sem lacuna material. Maior capacidade não autoriza redesenhar o Figma nem planejar detalhadamente todas as seções antecipadamente.
- Recomendar modo e motivo por bloco; informar modelo/esforço configurado só quando verificável. Não afirmar troca automática por prompt. Se depender de Gabriel, orientar a troca apenas entre opções reais antes do bloco seguinte.
- Após duas tentativas fundamentadas sem avanço sobre a mesma causa, mudar diagnóstico; usar maior capacidade quando apropriado e voltar ao econômico após resolver. Não confundir falta de ferramentas/acesso com falta de raciocínio.
- Validar com Gabriel mudanças materiais antes de implementá-las e cada etapa renderizada antes de avançar. Não pedir novamente decisões já aceitas. Preservar a verificação visual em qualquer modo.

## Conclusão e evidências
- Executar checks pertinentes; comparar a renderização com o frame Figma nas mesmas dimensões e conferir a adaptação nos dois eixos conforme a filosofia de layout.
- Conferir assets/fontes, links/menu/CTA, teclado/foco/rótulos, console e ausência de transbordamento horizontal.
- Captura da própria versão anterior serve para regressão, não para comprovar fidelidade ao Figma.
- Devolver branch/commit ou patch, comandos e resultados, capturas/preview, limitações e próximo passo. Não declarar pronto/testado sem a evidência correspondente.
- Ao entregar a etapa, parar para revisão da coordenação e validação visual de Gabriel. Corrigir a mesma etapa quando necessário; não iniciar a próxima seção por conta própria. Sem renderização/comparação comprovada, registrar “implementado; validação visual pendente” e preparar o handoff de verificação. Preview de revisão não equivale a deploy de produção.
