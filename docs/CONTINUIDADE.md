# GABiSOU — continuidade do site

## Produção confirmada em gabisou.com — 08/11/2026

- Site publicado e aberto com sucesso em `https://gabisou.com/`. Projeto Netlify existente `gabisou-landing-page`, ID `46afdf5f-6029-4908-abd6-2fe41eeeeae5`.
- Deploy de produção `6af01dac5c3eec5e25f7075a`, estado `ready`, publicado em 08/11/2026 às 03:58:59 (America/Sao_Paulo). Origem confirmada pelo plugin: `gabisou/gabisou.github.io`, branch `main`, commit `3e6028c63b0302fdd0b35112e2fbcc324c24d156`.
- Browser confirmou conteúdo do redesign, CSS carregado, imagens carregadas, fonte em estado loaded, inicialização do menu, robots `index, follow` e canonical `https://gabisou.com/`. Isso é uma conferência de publicação, não uma nova auditoria visual/completa de acessibilidade.
- Não há mais bloqueio de acesso para acompanhar o projeto pelo plugin Netlify. As notas anteriores sobre autenticação e vínculo pendentes são históricas e foram superadas por este deploy.
- Fluxo vigente: tarefas em branches a partir da `main`, checks/revisão da etapa, PR e merge na `main`. A atualização deste registro serve também para conferir o próximo deploy automático após o merge; verificar o commit/deploy retornado pelo Netlify.
- Próxima ação de produto: designer revisar a versão em produção e registrar decisões por seção. Desenvolver somente o próximo escopo aprovado; cada merge na main deve atualizar a produção após o build.

## Fluxo vigente de branches e produção — 08/11/2026

- Decisão: `main` é a branch de integração e produção. `codex/figma-redesign` é a branch de trabalho do redesign; não deve ser selecionada como origem de produção no Netlify.
- Gabriel autorizou integrar a versão atual aprovada e publicar em `https://gabisou.com`. Base verificada: `main@12a9196889ef93bf3597765daa360a286bb5e761`, redesign `c27ad52ef033f698c5d4245af8273eb2239fd0fc`, 17 commits à frente e nenhuma divergência da main.
- Próximas alterações: partir da `main` atualizada em uma branch de tarefa, implementar, executar checks pertinentes e obter a revisão/validação da etapa; integrar por pull request. Cada merge/push na `main` deverá iniciar build e deploy automáticos no projeto Netlify existente `gabisou-landing-page` (ID `46afdf5f-6029-4908-abd6-2fe41eeeeae5`), depois de concluir o vínculo.
- A fonte editável permanece em `dist/`; `netlify.toml` prepara e verifica `build/` para produção. Nenhuma alteração visual nesta decisão. Reversão de versão publicada: reverter o commit na `main` e publicar a correção pelo mesmo fluxo.
- Plugin Netlify conectado e leitura do projeto confirmada; a ferramenta não expõe alteração do repositório/branch de produção nem disparo de deploy. Último deploy confirmado: `67eef6c2dd395b00086bd7d1`, do repositório antigo `gabrieldevsouza/gabisou-landing-page`, commit `41e072063c06ec1880b5f24eb509e64e02e4f47a`.
- Há dois repositórios homônimos: `gabrieldevsouza/gabisou.github.io` (pessoal, somente main) e `gabisou/gabisou.github.io` (organização, fonte correta e privada). No Netlify selecionar o segundo, branch `main`. O painel está sendo operado por Gabriel para concluir esse vínculo; deploy atual ainda não confirmado.
- Validação reutilizada da mesma implementação e configuração: checks de fonte e release PASS (15 links, 15 IDs, 2 imagens), sintaxe JS e TOML válidas. A integração documental não exige uma nova revisão visual. Confirmar SHA final do merge e primeiro deploy antes de declarar a produção atualizada.

## Produção autorizada em gabisou.com — 08/11/2026

- Gabriel considerou o visual atual suficiente e autorizou publicar a versão como está para a designer testar e orientar as próximas etapas. Isso substitui a pausa de publicação do checkpoint anterior; não criar outra hospedagem ou domínio de revisão.
- Destino autorizado: projeto Netlify existente `gabisou-landing-page`, domínio `https://gabisou.com`. Fonte do redesign: `gabisou/gabisou.github.io`, branch `codex/figma-redesign`, base `e9bdcd8f14decd9bf3c5af068c74bc448ef58ca7`. Layout e conteúdo preservados.
- `netlify.toml` preparado: checks antes de cada build; produção limpa somente a saída gerada `build/`, executa `prepare_release.py --origin https://gabisou.com --output build` e valida `check.py build --public`. Fontes permanecem em `dist/`. Python 3.12; Node usado apenas no check de sintaxe do JS.
- Validação local da configuração: comando completo de produção PASS (15 links, 15 IDs, 2 imagens); sintaxe JS e TOML válidas; saída antiga de build removida no teste. Nenhuma instalação ou mudança de layout. Build remoto do Netlify ainda não executado.
- Integração pendente: vincular o projeto existente ao repositório `gabisou/gabisou.github.io` e selecionar `main` como branch de produção. A recomendação anterior de publicar diretamente `codex/figma-redesign` foi corrigida. Confirmar builds ativos, primeira execução e resposta de `gabisou.com`; alterações locais e pushes em branches de tarefa não atualizam produção.
- O screenshot mostra deploy antigo `main@41e0720`, enquanto `main` do repositório indicado está em `12a9196889ef93bf3597765daa360a286bb5e761`: não presumir que a integração já aponta para este repositório.
- Acesso: GitHub autenticado no navegador como `gabisoudev`. Netlify respondeu que a conta com o mesmo e-mail já existe e solicita acesso pelo método cadastrado; login Netlify ainda não concluído. Não alterar credenciais nem criar nova conta.
- A publicação feita indevidamente em outro serviço foi rejeitada por Gabriel e teve o acesso público removido. Não reutilizá-la como destino de publicação.
- Próxima ação: autenticar na conta Netlify existente, conferir a integração e concluir o deploy de produção. Reversão após publicar: republicar o último deploy válido do mesmo projeto; o identificador deve ser registrado quando o painel estiver acessível.
- Referências oficiais consultadas em 08/11/2026: [configuração por arquivo](https://docs.netlify.com/build/configure-builds/file-based-configuration/), [dependências de build](https://docs.netlify.com/build/configure-builds/manage-dependencies/) e [deploy de produção](https://docs.netlify.com/deploy/deploy-types/production-deploy/).

## Checkpoint remoto — 07/11/2026

- Branch de trabalho: `codex/figma-redesign`; stack HTML/CSS/JS nativo, fontes editáveis em `dist/index.html`, `dist/styles.css`, `dist/header.js` e assets em `dist/assets/`. Verificação: `python -X utf8 scripts/check.py`; prévia: `python -m http.server 8000 --bind 127.0.0.1 --directory dist`.
- Implementado no checkout: header, hero textual/CTAs, Serviços, Projetos de prévia, Quem somos, Como trabalhamos com quatro etapas e FAQ integrado, Contato e footer. FAQ está abaixo das etapas e “Antes de começar” foi removido. Cargos atuais: Gabriel `Desenvolvedor Fullstack`; Carol `Designer UX/UI`. Quem somos usa círculos no lugar de fotos. Projetos permanece uma etapa posterior.
- Verificado tecnicamente nesta preparação: checks Python e `git diff --check`; aprovação visual do usuário: nenhuma das seções novas está declarada aprovada. A última captura do footer foi rejeitada; depois houve correção estrutural para Grid de cinco áreas, identidade agrupada e SVGs reconhecíveis, ainda aguardando aceite visual.
- Pendências: comparação visual final de todas as seções; exportações Figma originais das quatro ilustrações de Como trabalhamos; vetores oficiais de Instagram, LinkedIn, retorno e copyright do footer; retratos de Quem somos. O footer usa `assets/figma/gabisou-wordmark.png` e SVGs locais fallback para os ícones, documentados como pendência.
- Destinos efetivos: CTA Contato preserva `mailto:gabisoudev@gmail.com` com assunto/corpo; Instagram `https://www.instagram.com/gabisoudev/`; LinkedIn `https://www.linkedin.com/in/gabrieldevsouza/`; logo/retorno `#inicio`.
- Próxima tarefa concreta: revisar visualmente o footer corrigido em 1920/1440/390px e substituir os SVGs fallback pelos vetores oficiais quando forem disponibilizados, sem avançar para publicação.

## Serviços — JSON_REST_V1 aplicado, 05/11/2026

- Conteúdo e estilos da seção foram substituídos pelo JSON transcrito do frame `02-services-desktop`/nó `1:417`: textos exatos, nove tags, cores, tipografia, raios e ordem interna. Tags agora ficam abaixo da descrição; o chevron foi removido por decisão de revisão e não deve voltar nesta etapa.
- Mantidos `#solucoes`, header, hero, CTAs, Projetos e demais seções. Em mobile, a numeração passa acima do card para preservar leitura; decisão inferida porque o JSON é desktop.
- Check Python e `git diff --check` desta rodada ainda pendentes. Captura original para comparação visual continua ausente.

## Serviços — diagnóstico e ajuste horizontal, 05/11/2026

- A porta 8000 servia uma cópia antiga; a inspeção real foi feita em `http://127.0.0.1:8001/`, servindo explicitamente `C:\Repos\gabisou.github.io\dist`. O DOM confirmou os textos JSON e a estrutura correta.
- Estilos computados em 1920 CSS px: container x112/1681px; lista x121/1663px; número 72×74px; card x246/1538×217.98px. O chevron medido anteriormente foi removido por decisão de revisão.
- Em 390px, linhas de 335px e scrollWidth 375px; sem transbordamento. Check Python PASS (19 links, 14 IDs, 2 imagens) e `git diff --check` PASS. Captura Figma original ainda pendente.

## Serviços — correção ao Figma bloqueada pela quota, 30/10/2026

- Branch `codex/figma-redesign`, HEAD `edd390691800cacbae84cc1044d7ce28a95b10f4`; alterações locais anteriores preservadas. Gabriel revogou a liberdade de inferir acabamento/textos de Serviços. A versão atual não é aprovada e não deve servir de referência visual.
- Cache local sem contexto completo/captura original de1:417. Uma chamada get_design_context com screenshot, após leitura da skill aplicável, retornou limite de chamadas do Figma MCP no plano Starter; nenhum contexto recebido. Sem repetição, exportação ou contorno por outra ferramenta. HTML/CSS não alterados nesta rodada.
- Insumo necessário: propriedades textuais completas e captura do frame1:417, incluindo textos/numeração/tags, cores/bordas, fontes/entrelinhas, raios/padding/gaps/alinhamentos e ícones/estados. Não é necessária arte exportada. [Referência e bloqueio](DESIGN-SERVICOS.md).
- Correção confirmada para a próxima implementação: tags abaixo da descrição em sua própria linha, alinhadas à direita no desktop; a coluna lateral da versão inferida está incorreta. Aguardar referência antes de editar um card e comparar. Header/hero/botões/Projetos e demais seções preservados. Sem fidelidade comprovada, push/publicação ou avanço para outra seção.

## Histórico — implementação inferida de Serviços, substituída pela exigência acima

- Branch `codex/figma-redesign`, HEAD `edd390691800cacbae84cc1044d7ce28a95b10f4`; alterações locais anteriores preservadas. Seção mantém #solucoes e o título introdutório. Categorias, descrições e nove tags existentes reaproveitadas na ordem sites → sistemas/aplicativos/integrações → automações/IA; sem novas promessas ou tecnologias.
- **Confirmado pela coleta informada por Gabriel:** frame1:417, introdução3:43 acima da lista3:42, três itens3:39/3:40/3:41, número fora da superfície, tags à direita no desktop, gap vertical aproximadamente32px, introdução próxima de x112 e cards aproximadamente1530×219. Não há extração visual detalhada local desta seção; nenhuma chamada nova ao Figma.
- Implementado section/h2 associado e lista ordenada com três linhas Grid `auto minmax(0,1fr)`, cada uma com número e article/h3/descrição/tags informativas. Container máximo1696px e lista1600px aproximam a composição ampla; altura dos cards pelo conteúdo, sem fixar219px. Setas antigas removidas: cards são estáticos, sem controles de expansão ou conteúdo oculto; interação futura depende de contrato.
- **Inferências a revisar:** fundo #F7F7F0, superfície #E9EFEC/raio22px e tags #C6D2CC/raio9px reutilizam componentes locais; roxo #4A36EB e Inter local preservam identidade. Títulos de card26px, corpo/tags16px e padding32px são decisões desta adaptação, não valores extraídos de Serviços. Grid interno texto/tags e Flex com quebra nas tags; min-width0 e quebra de texto nos filhos.
- Responsividade inferida pelo encaixe estimado: até70em (1120px), tags abaixo do texto/alinhadas ao início e padding24px; até40em (640px), número acima do card, padding20px, gap entre linhas24px. Fontes dos cards mantidas; espaços cedem primeiro. Nenhum overflow escondido ou escala artificial. Revisar encaixe em1920/950/390px; não afirmar fidelidade visual sem contexto/captura detalhados.
- Check Python PASS (19 links, 14 IDs, 2 imagens). Conferência estática confirmou header/hero/botões/Projetos e HTML/CSS externo a Serviços intactos, incluindo header.js e documentos anteriores. Servidor existente entrega HTML atualizado em `http://127.0.0.1:8000/#solucoes` (HTTP200 não comprova renderização). Captura em segundo plano não disponível pelas ferramentas desta sessão; pendentes visual/overflow/zoom e acionamento das âncoras no browser. Diff da etapa: `artifacts/servicos-2026-10-30/servicos.patch`. Parar para revisão humana, sem push/publicação ou alterações em Projetos; ilustração do hero continua pendente.

## Contrato vigente — duas ações do hero, 30/10/2026

- Substitui integralmente CTA/auxiliar anteriores: “Conheça mais” → #solucoes; “Conte o seu desafio” + seta decorativa → #contato. IDs existentes confirmados. Mesma ordem no HTML e na tabulação; sem JavaScript novo.
- ≥1440px: grupo Flex lado a lado, alinhado ao início, largura por conteúdo/padding; 810–1439px: coluna, width100%/max-width300px; <810px: coluna preenchendo a largura disponível, sem limite300px. Gap12px em todas as faixas, sem alterar o Grid texto/arte ou seus breakpoints.
- Acabamento corrigido: Inter local declarada explicitamente nos links, peso500/16px, linha1.4 e letter-spacing:normal; padding8px 23px, borda0 e mínimo38,4px, com crescimento por texto. Primário #4A36EB/branco/raio7px; secundário #C6D2CC/preto/raio7,4px. Raios são adaptações proporcionais (18×38,4/99 e 10×38,4/52), não novos valores extraídos do Figma. Texto/seta centralizados como conjunto, gap10px; SVG decorativo20×20/desenho12×12 preservado. Foco usa a mesma variável de raio e sobrepõe o arredondamento global de3px; sem regra999px, sombra ou gradiente no grupo. HTML, destinos e responsividade intactos; comparação visual ampla/intermediária pendente por falta de captura em segundo plano nesta sessão.
- Branch `codex/figma-redesign`, HEAD `edd390691800cacbae84cc1044d7ce28a95b10f4`; trabalho local anterior preservado. Somente grupo HTML, suas regras CSS e este registro alterados. Captura em segundo plano não exposta nesta sessão; validação renderizada do grupo em1920/950/390px e interação/foco permanece pendente. Parar para revisão humana, sem push/publicação.

- Checks desta rodada: Python PASS (19 links, 14 IDs, 2 imagens) e `git diff --check` aprovado. Conferência estática do diff confirmou HTML/CSS externos ao grupo e header.js intactos. Diff delimitado: `artifacts/hero-acoes-2026-10-30/acoes-do-hero.patch`.

## Correção vigente — responsividade intermediária do hero, 30/10/2026

- Branch `codex/figma-redesign`, HEAD `edd390691800cacbae84cc1044d7ce28a95b10f4`; trabalho local da entrega parcial preservado. A antiga media query `max-width:90em` causava empilhamento até1440px. Substituída pela faixa810–1439px com Grid `minmax(0,600px) 425px`, gap8px, centralização horizontal/vertical e padding24px 40px, sem somar a margem anterior.
- Nessa faixa, título/descrição separados por24px e CTA/auxiliar por44px do bloco anterior. Fonte preservada; trecho azul inline permite quebra natural. Texto com mínimo0; slot de arte425×525px e futuro img com object-fit:contain. O conjunto cresce se o texto ultrapassar525px. Abaixo de810px, uma coluna/gap32px e arte proporcional limitada ao container; a partir de1440px, composição ampla anterior preservada.
- HTML, destinos, header.js, header/Projetos e demais seções não alterados nesta correção. Sem captura em segundo plano disponível: evidência renderizada em950px pendente, assim como conferir810/390px e ausência de overflow. Valores derivados do CSS, não medidos no browser: com largura útil950px, 870px internos = texto437 + gap8 + arte425; com largura útil810px, texto297 + gap8 + arte425. Barra vertical reduz a largura útil e a coluna de texto.
- `git diff --check` aprovado; check de links não repetido, pois HTML intacto. Conferência estática confirmou header/JS, demais seções e regras base amplas preservados. Diff desta correção: `artifacts/hero-responsivo-2026-10-30/correcao-responsiva.patch`. Contrato atualizado também em DESIGN-HERO.md; parar para revisão humana, sem commit/push ou publicação.

## Histórico — hero, entrega parcial de texto/CTA, 30/10/2026 (Brasília)

- Pacote de Gabriel extraído em docs/design: HERO-ETAPA-1.md, contexto MCP e PNG de referência 1024×576; nenhum arquivo existente sobrescrito e nenhuma consulta nova ao Figma. Checkpoint local **edd390691800cacbae84cc1044d7ce28a95b10f4** preserva as alterações anteriores de header/ordem do menu/Projetos, documentação/evidências e os três arquivos recebidos. Sem temporários/ZIPs ou push; implementação do hero segue sem commit.
- Novo hero: título em duas partes 40px/500 e 40px/700 azul #4A36EB; descrição24px; CTA “Entre em contato”, nominal303×99/32px, fundo #4A36EB; fundo da seção #F5F7F0. Inter local restrita ao componente. Grid texto/arte, altura pelo conteúdo; margem84px e título171px abaixo do fim do header na referência1920px, sem restaurar header antigo. Gaps90/58/16px são limites desktop fluidos.
- Adaptação inferida: empilhar a composição até90em; título móvel mínimo28px, corpo18px, CTA20px e altura mínima64px. Espaços diminuem antes da tipografia. Região da arte fica abaixo do texto/ação no mobile. Sem escala artificial ou ocultação de conteúdo.
- Sem WhatsApp confirmado no HTML/documentação local: CTA provisório #contato, auxiliar “Fale diretamente com a equipe.” conforme contrato. Arte V3 removida da composição; somente “Ilustração em preparação” no slot reservado. Exportação estática oficial, efeito de lente e risco sobre AI FIRST ainda pendentes; não usar a captura como asset nem a exportação histórica incompleta.
- Header aprovado, header.js, Projetos e outras seções devem permanecer iguais ao checkpoint. Comparação visual pendente em1920/390px e uma largura intermediária, foco e destino do CTA: captura em segundo plano não exposta nesta sessão; não controlar a interface nem instalar ferramentas. Aguardar revisão humana desta parte antes de importar a arte ou iniciar Serviços. Resultados dos checks direcionados em VERIFICACAO.md.
- Verificação concluída: header/JS, HTML externo ao hero e regras CSS das demais seções iguais ao checkpoint; Python PASS (18 links, 14 IDs, 2 imagens) e diff-check sem erros. A redução de19 para18 links decorre da remoção do link auxiliar legado “Encontre seu ponto de partida” junto da composição antiga. Servidor existente entrega o HTML atual em `http://127.0.0.1:8000/`; isso não comprova renderização. Diff desta parte em `artifacts/hero-etapa-1/hero-etapa-1.patch`.

## Histórico — header com geometria Mirai, 30/10/2026 (Brasília)

- Ordem do menu alinhada às seções reais do main: SERVIÇOS (#solucoes) → PROJETOS (#projetos) → QUEM SOMOS (#sobre) → COMO TRABALHAMOS (#como-trabalhamos) → CONTATO (#contato). Somente links reordenados no HTML compartilhado por desktop/mobile; textos, destinos, CSS/JS e seções preservados. Leitura, visual e tabulação seguem essa mesma ordem do DOM. Check de links e diff-check integram esta rodada; parar para revisão humana.
- Nova orientação de Gabriel substitui as dimensões/breakpoints anteriores. Base real `eaa38db79d388901e273abb4d54ad6fa8703158d`, branch `codex/figma-redesign`; trabalho local anterior preservado. Somente header, referência em DESIGN-HERO.md e estas linhas alterados nesta rodada.
- Containers 1440/1226px, paddings externos 108/28/20px e internos 20/16/8px; marca proporcional 162/130/128px; Inter local 14px nominal, 400, linha1.7, tracking-.03em. Header fechado nominal 80px com crescimento pelo conteúdo. Gaps 12–24px acomodam os rótulos perto de 810px; Contato independente com 154,3×40px, dentro da expansão no mobile.
- CSS e JS sincronizados em `(width < 810px)`. Navegação completa em 810–1439px; desktop amplo a partir de 1440px. Projetos continua link normal. Valores e coordenadas calculadas, explicitamente separados das medidas da Mirai, em [DESIGN-HERO.md](DESIGN-HERO.md#header-vigente--geometria-mirai-e-identidade-gabisou-30102026).
- Checks desta rodada: Python PASS (19 links, 14 IDs, 2 imagens); Node e `git diff --check` aprovados. Comparação com a cópia local anterior confirmou HTML/CSS fora do header preservados; README.md e VERIFICACAO.md intactos. Diff delimitado em `artifacts/header-mirai-2026-10-30/diff-desta-rodada.patch`.
- Servidor existente reutilizado em `http://127.0.0.1:8000/`. Captura em segundo plano não exposta nesta rodada; comparação visual pendente em ~950/1920px, transição 810px e Menu em 390px. Sem controle da interface, pesquisa repetida, instalação, commit/push ou publicação. Parar para revisão do header; hero/Projetos fora da rodada.

## Histórico — ajuste anterior do header em 30/10/2026, substituído pela referência Mirai

- Base/HEAD permanece `eaa38db79d388901e273abb4d54ad6fa8703158d`, branch `codex/figma-redesign`; trabalho local anterior preservado. Esta rodada altera somente estilos/JS do header e estas linhas de continuidade.
- O limiar local encontrado era 96em, não 95em. Espaços fixos recolhiam a navegação já em 1440px; agora o Grid acomoda a distância marca/navegação e o Flex acomoda os intervalos antes do Menu. Em 1920px mantêm 185/56px; marca 260×77, Inter 22px e Contato 170×52 preservados. CSS e matchMedia passam juntos a 83em (1328px com raiz de 16px), dimensionado pelo conteúdo e com folga sobre seu encaixe estimado. Substitui o breakpoint registrado em 29/10.
- Checks: Python PASS (19 links, 14 IDs, 2 imagens); `node --check dist/header.js` aprovado. Conferência de escopo confirmou HTML, Projetos e CSS posterior ao header inalterados. `git diff --check` integra a conferência final.
- Servidor local ativo em `http://127.0.0.1:8000/` (somente dist/, bind loopback; PID observado 40020). Captura em segundo plano/IAB não exposta pelas ferramentas desta rodada; nenhum navegador visível controlado. Comparação visual pendente: 1920px contra a referência, navegação inline em 1440px e Menu no fluxo em 390px, incluindo Projetos/foco. Parar para revisão do header; sem novo relatório/ZIP, commit/push ou avanço ao hero.

## Estado atual — header e Projetos implementados; revisão humana pendente, 29/10/2026 (Brasília)

- Clone local `C:\Repos\gabisou.github.io`, padrão `C:\Repos` informado por Gabriel. Branch `codex/figma-redesign`; HEAD/base `eaa38db79d388901e273abb4d54ad6fa8703158d`. `git fetch origin` e fast-forward seguros, sem reset/stash: o remoto alterava somente o contrato de arquitetura, DESIGN-PROJETOS.md e sua captura. Os três documentos locais e a captura de setup foram preservados na incorporação; documentação foi atualizada depois, mantendo o histórico abaixo.
- Nova decisão de Gabriel substitui o estado pendente do menu: Projetos agora é link normal para `#projetos`, após Serviços e antes de Sobre. Três cards repetem somente “Titulo do projeto1”, “IMG”, “Resumo breve de projeto” e duas “Palavra-chave”. “Ver mais →” é botão nativo desabilitado; destino e conteúdo real ainda pendentes. Sem aviso de prévia no menu.
- AGENTS.md, contrato do header e [DESIGN-PROJETOS.md](DESIGN-PROJETOS.md) lidos explicitamente. Extração e PNG local reutilizados, sem nova consulta ao Figma. Header: 25:55; Projetos: 1:470, componentes 27:318/25:173/25:35. Referências, cores e geometria permanecem nesses contratos.
- Layout: Grid estrutura header, seção e cards; Flex organiza marca/Menu, navegação e tags. Container de Projetos limitado/centralizado; Grid passa de três para duas/uma coluna conforme espaço. Cards crescem pelo conteúdo; mídia tem proporção preferencial 517:255, permitindo altura maior sob ampliação/texto longo para não cortar conteúdo. Marca mantém proporção e limites; grupo marca/Menu quebra em linhas quando necessário.
- Header: breakpoint ajustado de 95em para 96em após testes preliminares de encaixe; estado final confirmado em 1536/1537 CSS px na origem localhost, sem o comportamento antigo em cache. Menu abre no fluxo; altura depende do conteúdo. Fechamento por âncora preserva foco no destino; Escape retorna ao Menu; mudança de largura transfere foco quando seu controle fica oculto.
- Diferenças assumidas: gaps iguais de 29,5 px entre cards, em vez de 26/33; IMG centralizado, em vez das posições assimétricas do frame; métricas das tags variam com a fonte local. Mobile é adaptação técnica sem frame aprovado. Detalhes mensurados e capturas separadas em [VERIFICACAO.md](VERIFICACAO.md).
- Checks finais PASS: 19 links, 14 IDs, 2 imagens; `node --check` e `git diff --check` sem erros. Matriz 1920/1440/768/390/320, altura baixa e paisagem, Menu, teclado, fallback sem script e texto ampliado verificados. Zoom real 200%/400% exercitado no Zen como complemento, com limites documentados.
- Evidências finais em [design/qa-header-projetos-2026-10-29](design/qa-header-projetos-2026-10-29/manifest.json): originais, viewport CSS/área útil/DPR/escala/pixels do arquivo e hashes. Identidade da versão = base acima + patch local de implementação SHA-256 `9be1076dd042a6f7c2f53f285973c082e2617bd1cd5e8c8e63e055f6ae229760`.
- Prévia: `http://localhost:8000/`, somente `dist/`, bind 127.0.0.1. Nenhuma instalação, configuração global, Caveman, commit/push, merge de branches, publicação ou DNS. Apenas fast-forward documental e alterações autorizadas de implementação/documentação/evidência. Hero, outras seções, assets e scripts de check preservados.

### Próxima tarefa

Coordenação revisa o diff e Gabriel valida visualmente **header e Projetos separadamente**, incluindo as diferenças registradas. Corrigir somente achados desta etapa quando solicitado. Não avançar ao hero. Conteúdo real/autorização de divulgação e destino de “Ver mais” permanecem pendentes antes de uma versão publicável.

## Histórico — header e setup em 28/10/2026 (orientações superadas pelo estado atual acima)

- Gabriel confirmou explicitamente o header atual 25:55 e Contato #C6D2CC. Referências/captura foram persistidas em e7f90ff094e8ad80f134fd8c3c5fa6f924e270e1; a implementação segue em commit separado, sem alterar hero/rodapé.
- Header implementado em HTML/CSS com Grid estrutural, navegação Flex, fonte local restrita ao componente e JS local com defer. Menu compacto expande no fluxo e tem fallback de links visíveis sem JS. Projetos permanece texto sem destino, identificado como “Pendente na prévia”; a seção real segue obrigatória no lançamento.
- Breakpoint inicial de 95em deriva da estimativa de encaixe; precisa ser validado no navegador. A altura de referência é obtida por conteúdo/padding, com crescimento permitido. Não há comparação renderizada concluída nem aceite visual da implementação.
- Componente atual: https://www.figma.com/design/XYP2AAZXyTlLTNvY2OphZX/GABiSOU-Site?node-id=25-55. Captura atual: docs/design/header-desktop-25-55-1920.png (1920 × 125). A captura anterior hero-desktop-1920.png está marcada como histórica para não validar o header antigo.
- Logo atual 25:15 exportado e comparado ao arquivo local: bytes e pixels idênticos. Manter gabisou-wordmark.png existente.
- Política de capacidade acrescentada por Gabriel: concentrar decisões difíceis/contratos no máximo ou maior capacidade; executar e ajustar blocos delimitados no econômico. Modelo/esforço reais dependem do cliente; nenhuma troca foi efetuada pela coordenação. O contrato do header deve ser reaproveitado; aprofundar só lacunas materiais.
- Pausa entre etapas: B entrega código/evidências; coordenação revisa; Gabriel valida visualmente antes de avançar. Se B continuar sem navegador funcional, C valida o mesmo commit no Windows. Não fechar etapa sem comparação ao Figma nem iniciar a próxima automaticamente.
- [ARQUITETURA-E-ETAPAS.md](ARQUITETURA-E-ETAPAS.md) registra recomendações, sequência, contrato preliminar do header, critérios de conclusão e decisões abertas. A V3 serve de base técnica, não de referência visual.
- Repositório: `gabisou/gabisou.github.io`; branch de trabalho `codex/figma-redesign`. O pacote de design parte do commit `178b83323eb8b9b49fc6fe2b7c98cb2ee989c5ae`. Base de implementação anterior: `857c326be11e4c335c4c508f8b4ee49995f590af` / PR #1 em rascunho.
- HTML/CSS editáveis em `dist/`; Python padrão para scripts; sem framework ou gerenciador de pacotes. Usar AGENTS.md.
- Diretriz de layout fornecida por Gabriel: Grid como primeira opção estrutural, Flexbox em grupos apropriados, componentes adaptados aos pais e comportamento explicado nos dois eixos. Incorporada em AGENTS.md e ARQUITETURA-E-ETAPAS.md; aplicada ao contrato do header e aos critérios de QA. Diretriz registrada no commit `eecd599fcb2dfb742bdb87e4fffc548e658b22a5`; a atualização atual também altera apenas documentação.
- GitHub: leitura, criação de branch, commits e gravação já comprovadas nesta coordenação. Leitura de PR/CI comprovada; criação de PR ainda não exercitada nesta rodada. Não há CI executado no commit base.
- A troca de conta Figma funcionou: `gabisougpt@gmail.com`, handle Gabriel, plano Starter, assento View. A conta anterior `gabisoudev@gmail.com` foi substituída nesta conexão. Acesso real ao arquivo e contexto/captura da abertura agora comprovados.
- Arquivo: [GABiSOU-Site](https://www.figma.com/design/XYP2AAZXyTlLTNvY2OphZX/GABiSOU-Site?node-id=1-200); fileKey `XYP2AAZXyTlLTNvY2OphZX`; página única `0:1`, Website — Desktop; alvo `1:200`, 01-hero-desktop, 1920 × 1080.
- [DESIGN-HERO.md](DESIGN-HERO.md) reúne referência atual do header e, em seção histórica, a extração anterior da abertura. Assets em dist/assets/figma/; Inter/licença em dist/assets/fonts/. Reaproveitar a extração atual; não reler todo o Figma.
- Sem mobile no arquivo lido. Gabriel escolheu botão Menu no mobile: expansão dos links no fluxo, com alternativa sem JS. A forma visual será uma adaptação, não um frame aprovado pela designer. Hero em coluna continua como proposta técnica.
- Arte decorativa estática exportada diretamente do Figma; manter HTML/CSS e evitar runtime React/WebGPU apenas para esse efeito sem animação/interação.
- WhatsApp ainda sem número/link confirmado. Gabriel definiu Projetos como obrigatório no lançamento: manter a seção no plano e exigir conteúdo real autorizado antes de publicar. O Figma possui placeholders e não há seção correspondente na V3; identificar pendências na prévia, sem inventar destinos/cases.
- B, segundo retorno de Gabriel: leitura GitHub e snapshot ec83e65 com 15/15 hashes conferidos; Python e check.py funcionaram. Git por terminal sem autenticação. Chrome remoto não alcançou localhost (bearer token/conexão recusada). Usar conector para persistência e encaminhar comparação visual a C se o impedimento permanecer.
- Neste ambiente, Playwright está instalado, mas Chromium/Firefox/WebKit apontam para executáveis inexistentes; uma tentativa de chromium.launch comprovou ausência do binário. Nenhum browser encontrado na busca limitada; nada instalado. A renderização será encaminhada à C.
- C: Windows, VS Code, Codex app/extensão e caminho local de renderização comprovados no setup abaixo. A próxima rodada será a comparação do header, após revisão humana do setup.
- Checks da implementação: python scripts/check.py aprovado (18 links, 12 IDs, 2 imagens); node --check dist/header.js aprovado. Casos direcionados do check aceitam JS local defer e rejeitam externo, inexistente, fuga de pasta e ausência de defer. HTTP 200 com bytes conferidos para HTML/CSS/JS/logo/fonte e logo legado. HTML fora do header/include preservado exatamente; estilos externos ao header preservados. Detalhes em VERIFICACAO.md.
- Domínio histórico: https://gabisou.com/. Hospedagem, DNS e fluxo de publicação seguem pendentes. Nova consulta em 28/10/2026 confirmou GitHub Pages desativado e zero execuções de Actions na branch de redesign; isso não descarta hospedagem externa existente. Nenhum deploy do redesign foi feito pela coordenação. Sem merge, publicação ou gasto autorizado nesta etapa.

### Setup local da executora C — 28/10/2026

- Padrão informado por Gabriel: `C:\Repos`. Clone criado em `C:\Repos\gabisou.github.io` com a autenticação Git existente, origem HTTPS conferida sem credenciais embutidas; branch `codex/figma-redesign`, HEAD `65eb45b3feb9bd8f8cfdac06ac71c533869ba735`, árvore inicialmente limpa.
- Windows 11 Pro local, PowerShell 7.6.9, aplicativo 26.1021.31345 (build 21828), VS Code 1.142.0 e extensão `openai.chatgpt` 26.1021.22027 identificados. Python 3.13.15 executado; Git 2.56.0.windows.3. Leitura explícita de AGENTS.md, README.md, Estado atual e diretriz/contrato de ARQUITETURA-E-ETAPAS.md; carregamento automático do AGENTS.md deste clone não comprovado.
- Check local: PASS, 18 links, 12 IDs, 2 imagens. Navegador integrado do aplicativo alcançou `http://127.0.0.1:8000/` no Windows e produziu [captura de setup](design/setup-local-65eb45b-1920x1080.jpg), viewport 1920 × 1080. CSS, fonte, logo e inicialização do JS conferidos; detalhes em [VERIFICACAO.md](VERIFICACAO.md#setup-local-windows--28102026).
- Caveman avaliado na referência solicitada, sem instalação: manter respostas concisas. A instalação completa documenta CLI/hooks e não comprova integração com este app/extensão; benchmarks não medem consumo de Gabriel.
- Somente documentação/evidência alteradas; nenhuma configuração, implementação, commit, push, merge ou publicação. Setup aguarda revisão humana. Comparação completa com Figma, comportamento responsivo/acessibilidade e aceite visual do header permanecem pendentes; não avançar ao hero.

### Próxima tarefa prevista em 28/10/2026 — superada pela decisão de 29/10

Após Gabriel revisar o setup, C: validar somente o commit de implementação entregue pela coordenação no Windows, seguindo o contrato e checklist em VERIFICACAO.md; entregar capturas/evidências. A coordenação revisa e Gabriel valida o resultado. Não avançar ao hero. Se forem necessárias correções, retornar achados com viewport/estado; uma executora altera os arquivos por vez.

Arquitetura recomendada: página única estática, HTML semântico, CSS por componente com tokens, Grid estrutural e Flexbox local, JS nativo somente para comportamentos necessários e biblioteca local de assets. Sem instalação/migração nesta rodada. O check já permite JS local existente dentro da pasta verificada, com defer; mantém a restrição de WhatsApp não confirmado. Outras evoluções só quando houver requisito real.

Preparação do repositório e acesso ao design concluídos; o caminho local de renderização foi comprovado no setup acima e aguarda revisão de Gabriel. A comparação completa do header é a etapa seguinte. No cliente Codex, distinguir carregamento automático de AGENTS.md de leitura explícita.

---

## Histórico anterior — V3

Atualizado em 27/10/2026 (Brasília). Estado atual: V3 implementada e revisada; ainda não publicada.

## Objetivo e restrições

Página comercial para conquistar clientes próprios de tecnologia, apoiar credibilidade e facilitar conversas, propostas e contratações. A prospecção continua independentemente do lançamento. Serviços gerais são a prioridade; jogos ficam em segundo plano. Não inventar equipe, resultados, clientes, cases, endossos ou condições comerciais. Não expor urgência financeira. Participação e remuneração da designer em futuros contratos ainda precisam ser combinadas.

## Ambiente

- Fonte local: `/workspace/sites/gabisou-v1`.
- Repositório privado existente: `gabisou/gabisou.github.io`.
- Branch de trabalho: `codex/site-comercial-v1`; PR de revisão: https://github.com/gabisou/gabisou.github.io/pull/1.
- Site atual: https://gabisou.com/. Hospedagem e DNS ainda não confirmados. Nenhum merge, publicação, domínio ou gasto alterado.
- HTML/CSS estáticos em `dist/`, sem dependências de produção ou JavaScript de execução. Prévia sem indexação.
- `scripts/prepare_release.py --origin https://gabisou.com --output build` gera versão indexável, canonical, sitemap e dados da organização. Apenas gera arquivos; não publica.
- Logotipo local obtido do site atual. E-mail confirmado publicamente: `gabisoudev@gmail.com`; recebimento não testado.
- Instagram `https://www.instagram.com/gabisoudev/` e LinkedIn `https://www.linkedin.com/in/gabrieldevsouza/` são os destinos publicados pelo site atual.
- Sem WhatsApp: nenhum número confirmado. Sem formulário, rastreadores, CMS, banco de dados ou checkout.

## Revisão V3 — referências e mensagem

As seis referências enviadas por Gabriel foram analisadas quanto a conteúdo e navegação. Cinco sites puderam ser lidos; Studio Mirai teve leitura bloqueada e seu LinkedIn institucional foi usado como fonte complementar, com a diferença indicada. `docs/REFERENCIAS-E-MENSAGEM.md` registra fontes, comparação e limites. Não houve auditoria visual ou de desempenho dos sites de referência.

Título explícito mantido. Texto de apoio parte de três necessidades: apresentar serviços, organizar a operação, automatizar tarefas. Serviços agora vêm antes de Sobre e apresentam problema, entrega e exemplos. Sobre: “Contato direto com quem desenvolve.” Processo e convite de contato ficaram mais concretos. Nenhuma promessa de resultado, equipe fixa ou oferta adicional foi incluída. Conteúdo continua proposto, sem aprovação editorial.

Estrutura atual: início → serviços → sobre → processo → contato → rodapé. CSS, identidade, contatos e ilustração existentes preservados. Menu e rodapé acompanham a nova ordem. Prévia portátil: `gabisou-previa-v3.html`, com estilos e imagens incorporados, sem dependências externas de apresentação.

Fonte local corresponde à branch remota de revisão; o ambiente local não contém `.git`. Persistência pelo conector GitHub, preservando a árvore e usando comparação do SHA esperado. Sem merge ou deploy.

## Histórico — evidências e decisões da V2

Gabriel enviou cinco wireframes produzidos pela designer: início, sobre, projetos, serviços e rodapé. Eles ainda contêm textos e imagens de preenchimento. A direção visual da V2 parte desse trabalho, com fundo `#FAF7F4`, cabeçalho `#418CC2`, azul escuro `#2C6795`, botões arredondados e menu Sobre/Serviços/Contato. A designer não foi apresentada como funcionária e seu nome ainda não foi informado.

Estrutura da V2: início → sobre → três grupos de serviços → processo → contato → rodapé. Design de interfaces aparece explicitamente no primeiro grupo. Os outros grupos são sistemas/aplicativos/integrações e automações/IA. Não foram presumidos serviços de publicidade, branding ou gestão de redes.

Título proposto: “Sites, sistemas e automações para sua empresa.” Apoio: “Do design de interfaces ao desenvolvimento, a GABiSOU ajuda a apresentar seus serviços, organizar informações e conectar as ferramentas usadas no dia a dia.” CTA principal: “Conversar sobre meu projeto”, por e-mail.

O texto inglês antigo sobre jogos foi substituído. Não há seção vazia de Projetos: ela será incluída quando houver materiais com autoria e divulgação confirmadas. O fluxo da primeira tela permanece identificado como exemplo ilustrativo.

Rodapé: logotipo, descrição de serviços, Gabriel/Jacarepaguá/Rio de Janeiro, navegação, e-mail e Instagram secundário. Sem endereço inventado, certificações, CNPJ deduzido ou alegações legais.

`docs/CONTEUDO-PARA-DESIGN.md` reúne os textos prontos, propostas de missão/visão e requisitos para futuros cards de projetos. Missão e visão são sugestões internas; não foram adicionadas como seções ao site. Todo o conteúdo e o processo ainda são propostas editoriais, não textos aprovados por Gabriel.

## Verificação

Consultar `docs/VERIFICACAO.md` para os resultados atuais e histórico da V2. Checagens de arquivos estáticos, release, links, responsividade e contraste executadas. Limites: sem teste de recebimento de e-mail, leitor de tela, aparelhos físicos ou dados de campo. Não declarar conformidade integral WCAG.

## Escopo e continuidade

| Para lançar | Depois de ouvir compradores | Fora desta versão |
| --- | --- | --- |
| Aprovação editorial, hospedagem confirmada e autorização da publicação com ação/custo claros | Cases autorizados, refinamento dos textos, WhatsApp confirmado | Blog, checkout, membros, chatbot, painel de analytics |
| Destino de contato correto e arquivos finais revisados | Nome e apresentação pública da designer, se combinados | Preço, desconto, suporte ou Black Friday sem aprovação |

Nenhum case é obrigatório para lançar. Não reabrir triagem financeira. Próxima tarefa: revisão de Gabriel/da designer, ajustes concretos e identificação da hospedagem atual antes de preparar a ação de publicação. Não enviar mensagens à designer sem solicitação explícita.

## Medição comercial simples

Registrar manualmente data, empresa/referência, origem declarada, necessidade, próximo passo, proposta enviada, contratação e recebimento confirmado. Um clique não é conversa; conversa não é pagamento. Não publicar esses registros no site.

## Fontes

Briefing de Gabriel nesta conversa; cinco wireframes anexados; site atual inspecionado; repositório existente; referências oficiais W3C/Google listadas no relatório de verificação. O site atual confirma contatos e identidade, não comprova contratos ou resultados comerciais.
## Quem somos — referência 05-about-desktop aplicada, 05/11/2026

- Seção `#sobre` substituída pela introdução e pelos perfis de Gabriel de Souza e Carol Faustino conforme JSON anexado. Desktop usa dois cards em Grid; adaptação mobile empilha perfis e move o retrato para cima abaixo de 480px.
- Retratos oficiais não existem nos assets locais; foram reservados espaços neutros 161×166px, sem fotos substitutas. Link LinkedIn de Gabriel preservado; Carol permanece sem link por falta de destino confirmado.
- Check Python PASS (19 links, 14 IDs, 2 imagens) e `git diff --check` PASS. Comparação visual final e troca dos retratos aguardam revisão humana.
## Como trabalhamos — referência 04-process-desktop aplicada, 07/11/2026

- Seção `#como-trabalhamos` substituída pelo conteúdo exato fornecido: introdução e quatro etapas numeradas 1–4. CSS isolado em `process-*`, com Inter local, fundo `#F7F7F0`, traços internos nos números e sem caixas/interações.
- Desktop usa container próprio e quatro trilhas de 420px com os deslocamentos do JSON; abaixo de 1450px duas colunas e abaixo de 700px uma coluna. Ilustrações reservadas em 208×135px, sem assets substitutos.
- Cargos aprovados de Quem somos permanecem `Desenvolvedor Fullstack` e `Designer UX/UI`, registrados também em `DESIGN-QUEM-SOMOS.md`.
- Comparação visual com o frame e exportação das quatro ilustrações pendentes. Check Python PASS (19 links, 14 IDs, 2 imagens) e `git diff --check` PASS. Renderização computada confirmou Inter 24px/29.0455px nas descrições, quatro etapas em desktop e uma coluna em 390px sem overflow.
## FAQ integrado a Como trabalhamos — referência 06-faq-desktop, 07/11/2026

- FAQ inserido abaixo das quatro etapas, na mesma section `#como-trabalhamos`; removido somente o antigo `Antes de começar`. Perguntas exatas mantidas, inclusive `Voces` sem acento.
- Lista sem respostas/interação: perguntas são texto e os sinais de mais têm `aria-hidden`. Grid desktop com introdução/lista; adaptação mobile empilha regiões e usa 64px de junção. O intervalo de 120px no desktop é decisão de integração.
- Check e comparação visual serão registrados após a rodada; captura do frame não está disponível nesta sessão.
## Contato — referência 07-contact-desktop aplicada, 07/11/2026

- Seção `#contato` mantém o título sem acento em `voce`, frase de apoio e CTA `Entre em contato`; o rótulo superior `Contato` foi removido por decisão de revisão.
- CTA preserva o `mailto` existente com assunto/corpo; não há seta, formulário, telefone ou endereço adicional. Estilos isolados em `contact-*`, com Grid desktop e empilhamento abaixo de 700px.
- Referência e decisões registradas em `DESIGN-CONTATO.md`. Comparação visual com captura e conferência computada após renderização permanecem pendentes nesta rodada.
## Footer — referência 08-footer-desktop aplicada, 07/11/2026

- Footer antigo substituído pela composição JSON: wordmark e frase no mesmo agrupamento `identity`, retorno, localização, Instagram, LinkedIn, copyright 2026. Camada oculta `Projetos` não foi representada.
- Wordmark usa asset Figma local; destinos Instagram e LinkedIn confirmados preservados. Vetores oficiais não estão nos assets; SVGs locais reconhecíveis substituem os círculos/quadrados rejeitados, com a pendência documentada em `DESIGN-FOOTER.md`.
- Grid desktop com altura mínima de referência 448px; abaixo de 900px reorganiza regiões e abaixo de 520px empilha. Comparação visual e medidas computadas aguardam revisão.
