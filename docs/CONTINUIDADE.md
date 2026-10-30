# GABiSOU — continuidade do site

## Foco atual — header com geometria Mirai, 30/10/2026 (Brasília)

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
