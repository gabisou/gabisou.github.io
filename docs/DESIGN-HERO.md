# Figma — cabeçalho e abertura GABiSOU

Extração em 28/10/2026, pelo MCP oficial, sem alterar o arquivo. Esta referência vale para a primeira parte da implementação, não para as demais seções.

## Fonte e escopo
- Arquivo: [GABiSOU-Site](https://www.figma.com/design/XYP2AAZXyTlLTNvY2OphZX/GABiSOU-Site?node-id=1-200).
- fileKey: `XYP2AAZXyTlLTNvY2OphZX`.
- Única página retornada: `0:1`, `Website — Desktop`. Nenhum frame mobile foi encontrado nessa página.
- Alvo: `1:200`, `01-hero-desktop`, 1920 × 1080.
- Filhos relevantes: cabeçalho `3:4`; navegação `3:3`; texto/CTA `3:24`; arte decorativa `3:25`; logo do cabeçalho `1:210`.
- `get_design_context` retornou contexto completo e captura do alvo. As medidas abaixo vêm desse contexto; não são deduções da V3.
- Referência visual: [hero-desktop-1920.png](design/hero-desktop-1920.png), 1920 × 1080. Usar somente para comparação, nunca como imagem da página inteira.
- Outras seções apenas inventariadas, não extraídas para implementação: Serviços `1:417`, Projetos `1:470`, Processo `1:513`, Sobre `1:552`, FAQ `1:582`, Contato `1:623`, Rodapé `1:640`. Existem camadas explicitamente nomeadas como placeholders.

## Especificação explícita do desktop
As coordenadas são relativas ao alvo 1920 × 1080. Traduzir a estrutura para layout responsivo; não escalar a página inteira.

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
- Navegação acessível: logo e contato no topo, demais links em uma segunda faixa que possa quebrar linhas. Preservar ordem do DOM e foco; evitar dependência de menu JavaScript nesta primeira prova.
- Conferir 390 × 844 e 320 × 740, além de 768 px e 1440 px de largura. Ajustar tipografia/intervalos de forma fluida preservando a hierarquia.
- Sem alturas fixas que cortem texto nem transbordamento horizontal. Arte decorativa com alt vazio.

## Comportamento e pendências materiais
- O número/link de WhatsApp não foi confirmado. Não inventar telefone nem ligar “Por whatsapp” silenciosamente a e-mail. Pode-se entregar uma prévia visual claramente identificada com CTA demonstrativo até o destino chegar; produção não está concluída.
- PROJETOS não tem âncora correspondente na V3 e os cards do Figma são placeholders. Não criar casos fictícios ou link quebrado. Na prévia, sinalizar o item como indisponível; manter a decisão de conteúdo/publicação pendente.
- Links existentes que podem funcionar: QUEM SOMOS → #sobre; SERVIÇOS → #solucoes; COMO TRABALHAMOS → #como-trabalhamos; CONTATO → #contato.
- Preservar textos, contatos e comportamento das demais seções. Não alterar o rodapé para reproduzir a primeira tela.
- Não tornar o cabeçalho sticky apenas porque ele aparece repetido nos frames; o comportamento de fixação não foi especificado.

## Verificação da primeira entrega
- Check estático pertinente: `python scripts/check.py`.
- Comparação obrigatória com a referência em 1920 × 1080 após carregamento da fonte; conferir tamanho e recorte de ambos os assets.
- Conferir reflow, links/CTA conforme estado demonstrativo, teclado/foco, nomes acessíveis, console e requisições.
- B não comprovou acesso do Chrome remoto ao seu servidor. Se isso permanecer, entregar código/preview identificado e encaminhar só a captura/verificação a C no Windows. Não repetir o diagnóstico de localhost sem nova evidência nem declarar fidelidade visual antecipadamente.
