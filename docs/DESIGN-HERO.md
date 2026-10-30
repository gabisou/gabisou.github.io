# Figma — cabeçalho e abertura GABiSOU

Extração em 28/10/2026, pelo MCP oficial, sem alterar o arquivo. Esta extração é compartilhada por duas entregas separadas: etapa 1 (header) e etapa 2 (hero). Consultar ARQUITETURA-E-ETAPAS.md antes de implementar; não executar ambos numa única tarefa.

## Header vigente — geometria Mirai e identidade GABiSOU, 30/10/2026

Gabriel substituiu as dimensões e os breakpoints anteriores do header pela coleta de HTML/CSS e DOM de [Studio Mirai](https://studiomirai.com.br/) fornecida nesta sessão. Coleta da referência informada por Gabriel, sem nova pesquisa nesta rodada. Identidade mantida do Figma 25:55: asset original proporcional, Inter local, textos/destinos, fundo #F7F7F0, Contato #C6D2CC e raio existente. Os 260px/22px/gaps 185/56px abaixo são histórico, não requisitos vigentes.

| Região | ≥1440px | 810px a <1440px | <810px |
| --- | --- | --- | --- |
| Wrapper centralizado | largura 100%, máximo 1440px | igual | igual |
| Padding externo horizontal | 108px | 28px | 20px |
| Container centralizado | máximo 1226px | máximo 1226px | máximo 580px |
| Padding interno horizontal | 20px | 16px | 8px |
| Marca GABiSOU | 162px × altura automática (~47,98px) | 130px × altura automática (38,5px) | 128px × altura automática (~37,91px) |

- Altura fechada nominal 80px incluindo bordas: container mínimo 78px, padding vertical 10px e alinhamento central. Altura cresce com conteúdo/expansão; a marca usa sua proporção 260:77, não as alturas da Mirai. Bordas laterais visuais em inset preservam a largura útil dos containers.
- Inter 400, .875rem (14px na raiz de 16px), line-height 1.7, letter-spacing -.03em. Gaps dos quatro links até 24px, flexibilizados até 12px perto de 810px. Contato com largura nominal independente 154,3px e altura mínima 40px; não depende do tamanho do rótulo.
- Grid externo distribui marca/restante; Grid aninhado no nav distribui coluna central `minmax(0,1fr)`/Contato automático. Flex centraliza os quatro links na coluna intermediária. Contato permanece no mesmo nav, separado da lista, para manter destino e comportamento da expansão.
- Abaixo de 810px, Menu expande o nav na linha seguinte, no fluxo; Contato ocupa a largura da expansão e tem altura mínima 44px. CSS e matchMedia usam a mesma condição `(width < 810px)`; em 810px a navegação permanece completa.
- **Calculado pelo CSS, não medido no browser desta rodada:** largura útil 950px → marca x44 e borda direita do Contato x906; largura útil 1348px → container x61/largura1226, marca x77 e Contato x1116,7/largura154,3. Com largura útil 1920px, wrapper x240, marca x368 e Contato termina em x1552; barra de rolagem reduz a largura útil e desloca a centralização.
- Implementado; comparação renderizada pendente. Captura em segundo plano não exposta nesta rodada; nenhum controle de mouse/teclado ou navegador visível. Conferir somente header em ~950/1920px, limite 810px e Menu em 390px antes de aceitar.

## Histórico — header Figma aprovado em 28/10/2026, etapa 1

Gabriel confirmou em 28/10/2026 o componente [Navigation/Site header 25:55](https://www.figma.com/design/XYP2AAZXyTlLTNvY2OphZX/GABiSOU-Site?node-id=25-55), incluindo Contato em **#C6D2CC**. Esta seção substitui a especificação anterior do header 3:4. O código do hero permanece fora do escopo.

- Contexto atual completo e captura obtidos pelo MCP; reutilizar esta extração.
- Referência vigente do header: [header-desktop-25-55-1920.png](design/header-desktop-25-55-1920.png), 1920 × 125, exportação isolada do componente.
- Estrutura: header 25:55; Brand/Logo/Wordmark 25:15; Navigation/Primary 25:44; Navigation/Link 25:42; contact-action 25:53, associado ao botão Secondary/Compact. O header é um componente compartilhado; isso não determina a stack.
- O componente declara referência desktop de 1920 px; não documenta comportamento mobile.
- Logo local `dist/assets/figma/gabisou-wordmark.png` confrontado com nova exportação isolada de 25:15: **bytes e pixels idênticos**, PNG RGBA 260 × 77, 7259 bytes, blob `fac14c9d46e4397158a0758458b6cc7135015a35`. Reutilizar o arquivo.

| Propriedade explícita no contexto atual | Valor de referência |
| --- | --- |
| Header | 1920 × 125; fundo #F7F7F0; borda 1 px #282836; alinhamento vertical central |
| Espaçamento horizontal interno | 29 px |
| Distância marca → navegação | 185 px |
| Marca | caixa 260 × 77; proporção preservada |
| Navegação | grupo linear com intervalo de 56 px |
| Rótulos | Inter Regular 400, 22 px; código de referência com line-height normal |
| Contato | fundo #C6D2CC; caixa 170 × 52; raio 10 px; padding horizontal 20 px e vertical 10 px; texto preto |

Ordem: QUEM SOMOS → SERVIÇOS → COMO TRABALHAMOS → PROJETOS → CONTATO. Destinos e Menu mobile seguem o contrato técnico já confirmado em ARQUITETURA-E-ETAPAS.md. Traduzir o layout do componente para Grid estrutural e Flexbox no grupo linear, com limites e crescimento por conteúdo; os valores acima não obrigam alturas rígidas sob zoom ou menu aberto.

A captura antiga `hero-desktop-1920.png` fica preservada como **referência histórica da extração anterior**. Seu header 3:4/Contato #D9D9D9 está desatualizado e não deve ser usado para aprovar a etapa 1. O restante do frame é contexto da extração anterior do hero; verificar a vigência apenas quando a etapa 2 começar.

## Fonte e escopo — extração histórica
- Arquivo: [GABiSOU-Site](https://www.figma.com/design/XYP2AAZXyTlLTNvY2OphZX/GABiSOU-Site?node-id=1-200).
- fileKey: `XYP2AAZXyTlLTNvY2OphZX`.
- Única página retornada: `0:1`, `Website — Desktop`. Nenhum frame mobile foi encontrado nessa página.
- Alvo: `1:200`, `01-hero-desktop`, 1920 × 1080.
- Filhos relevantes: cabeçalho `3:4`; navegação `3:3`; texto/CTA `3:24`; arte decorativa `3:25`; logo do cabeçalho `1:210`.
- `get_design_context` retornou contexto completo e captura do alvo. As medidas abaixo vêm desse contexto; não são deduções da V3.
- Referência visual: [hero-desktop-1920.png](design/hero-desktop-1920.png), 1920 × 1080. Usar somente para comparação, nunca como imagem da página inteira.
- Outras seções apenas inventariadas, não extraídas para implementação: Serviços `1:417`, Projetos `1:470`, Processo `1:513`, Sobre `1:552`, FAQ `1:582`, Contato `1:623`, Rodapé `1:640`. Existem camadas explicitamente nomeadas como placeholders.

## Especificação explícita do desktop — histórica
As coordenadas são relativas ao alvo 1920 × 1080. Traduzir a estrutura para layout responsivo; não escalar a página inteira. Seguir a filosofia de layout em ARQUITETURA-E-ETAPAS.md: Grid como primeira opção estrutural, Flexbox nos grupos adequados e adaptação aos pais. Dimensões do frame são referências de comparação, não alturas fixas para seções/header; permitir crescimento pelo conteúdo e preservar proporções dos assets.

| Elemento | x, y | Dimensões e estilo |
| --- | --- | --- |
| Fundo da abertura | 0, 0 | #F5F7F0 |
| Cabeçalho | 0, 0 | 1920 × 125; #F7F7F0; borda 1 px #282836 |
| Logo | 29, 26 | 260 × 77; manter recorte e transparência do asset |
| Navegação | 474,48, 36 | grupo 1013,52 × 52; Inter 400, 22 px, altura de texto 27 px |
| Contato no menu | 1318, 36 | 170 × 52; #D9D9D9; raio 10 px; texto preto |
| Título | 84, 296 | duas linhas, 721 × 96; 40 px; altura aproximada de linha 48 px |
| Apoio | 85, 482 | 909 × 58; Inter 400, 24 px; altura aproximada de linha 29 px |
| CTA principal | 85, 598 | 303 × 99; #4A36EB; raio 18 px; texto branco Inter 500, 32 px |
| Texto auxiliar | 85, 713 | Inter 400, 16 px; altura 19 px |
| Arte | aproximadamente 932, 174 | asset exportado 935 × 907; referência recorta a arte no fim do frame |

Ordem visual do menu: QUEM SOMOS → SERVIÇOS → COMO TRABALHAMOS → PROJETOS → CONTATO.

Texto exato do título:
1. Desenvolvimento de soluções digitais — Inter 500, preto.
2. para a realidade da sua empresa. — Inter 700, #4A36EB.

Apoio: “A GABiSOU transforma necessidades do seu negócio em soluções digitais, com execução técnica e conversa próxima.”
No desktop, a quebra observada vem depois de “com”.

CTA: “Entre em contato”.
Auxiliar: “Por whatsapp, direto com Gabriel”.

A tipografia do Figma é Inter. O retorno usa line-height normal; as alturas acima orientam a comparação, não comprovam um token global. Não foi feita uma leitura separada de variáveis globais.

## Assets e fonte já preparados
- `dist/assets/figma/gabisou-wordmark.png`: rasterização isolada do nó `1:210`, 260 × 77, PNG transparente.
- `dist/assets/figma/hero-artwork.png`: rasterização isolada da arte `3:25`, 935 × 907, PNG transparente, incluindo painéis, monograma, brilhos, sombras e efeito.
- Os dois assets foram recebidos diretamente pelo MCP em PNG/base64. O download HTTP externo devolveu uma página “Site Unavailable”, portanto não usar esse caminho nem salvar HTML com extensão PNG.
- A arte tem efeito “Lens distortion”; o manifesto retornado declara `isAnimated: false` e `usesMouse: false`. Decisão técnica: conservar a aparência por exportação direta estática da arte, sem redesenhá-la em CSS e sem adicionar React/WebGPU ao site. Apenas a ilustração é raster; textos, navegação e botões devem ser HTML acessível.
- O asset da arte já contém o recorte inferior do frame desktop. Não reconstruir a parte que está fora da referência. Conferir proporção, transparência e encaixe no desktop antes de reaproveitar no mobile.
- `dist/assets/fonts/InterVariable.woff2`: fonte normal variável oficial Inter v4.1; cobre pesos 100–900. Origem fixada: repo `rsms/inter`, commit `e3a3d4c57d5ecc01453a575621882a384c1995a3`, caminho `docs/font-files/InterVariable.woff2`; blob `5a8d3e72ad7ffb62af3b146e1b1f54ab5813a212`.
- Licença integral junto à fonte em `dist/assets/fonts/Inter-LICENSE.txt`. Não depender de CDN. A versão exata da Inter usada no Figma não foi identificada; verificar métricas no resultado visual.
- Registrar @font-face normal com pesos 100 900; carregar somente os pesos usados 400/500/700. Evitar mudança global da fonte nas seções fora do escopo.

## Adaptação mobile — proposta técnica, não frame aprovado
- Usar fluxo normal em coluna: título, apoio, CTA/auxiliar e arte.
- Margens mínimas de 20 px; manter proporções da arte e limitar sua largura ao espaço disponível.
- Navegação mobile não foi especificada no Figma. Gabriel escolheu botão Menu que expande os links no fluxo. Consultar ARQUITETURA-E-ETAPAS.md para comportamento, fallback e QA; não apresentar a adaptação visual como frame aprovado pela designer.
- Conferir 390 × 844 e 320 × 740, além de 768 px e 1440 px de largura. Ajustar tipografia/intervalos de forma fluida preservando a hierarquia.
- Sem alturas fixas que cortem texto nem transbordamento horizontal. Arte decorativa com alt vazio.

## Comportamento e pendências materiais
- O número/link de WhatsApp não foi confirmado. Não inventar telefone nem ligar “Por whatsapp” silenciosamente a e-mail. Pode-se entregar uma prévia visual claramente identificada com CTA demonstrativo até o destino chegar; produção não está concluída.
- PROJETOS é obrigatório no lançamento por escolha de Gabriel. Ainda não tem âncora correspondente na V3 e os cards do Figma são placeholders. Não criar casos fictícios ou link quebrado. Na prévia, sinalizar o item como pendente até a etapa 4; publicação exige conteúdo real autorizado.
- Links existentes que podem funcionar: QUEM SOMOS → #sobre; SERVIÇOS → #solucoes; COMO TRABALHAMOS → #como-trabalhamos; CONTATO → #contato.
- Preservar textos, contatos e comportamento das demais seções. Não alterar o rodapé para reproduzir a primeira tela.
- Não tornar o cabeçalho sticky apenas porque ele aparece repetido nos frames; o comportamento de fixação não foi especificado.

## Verificação por etapa
- Check estático pertinente: `python scripts/check.py`.
- Etapa 1: comparar a região do header em viewport 1920 × 1080 com a captura atual header-desktop-25-55-1920.png (1920 × 125), após carregar a fonte; preservar o hero existente. A captura histórica do hero não é referência do header. Etapa 2: conferir a vigência da referência antes de comparar a abertura completa.
- Conferir reflow nos dois eixos, redimensionamento contínuo, janela baixa/paisagem, textos longos e ampliação de texto/zoom, conforme o contrato da etapa. Verificar links/CTA conforme estado demonstrativo, teclado/foco, nomes acessíveis, console e requisições. Registrar o que ficou sem teste.
- B não comprovou acesso do Chrome remoto ao seu servidor. Se isso permanecer, entregar código/preview identificado e encaminhar só a captura/verificação a C no Windows. Não repetir o diagnóstico de localhost sem nova evidência nem declarar fidelidade visual antecipadamente.
