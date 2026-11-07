# Serviços — referência JSON_REST_V1 aplicada

Fonte: JSON transcrito do frame `02-services-desktop`, nó `1:417`, 1920×1080. A captura original continua pendente; portanto a conformidade abaixo é textual/geométrica, não uma comparação visual comprovada.

## Conteúdo e acabamento confirmados

- Introdução somente `Serviços` e `Qual o próximo passo da sua empresa?`.
- Três linhas: `01` Sites e presença digital; `02` Sistemas, aplicativos e integrações; `03` Automações e aplicações. Cada card usa a descrição e as três tags transcritas no HTML.
- Fundo da seção `#F7F7F0`; cards e caixas de número `#E9EFEC`; tags `#C6D2CC` com texto `#4A36EB`; sem bordas ou sombras.
- Inter: rótulo 26/31.47 peso300; título 48/58.09 peso500; cards 32/38.73 peso600; descrições 24/29.05; números 34/41.15; tags 15/18.15. Raio do número 21px, card 41px e tag 24px.
- Tags ficam abaixo da descrição, em linha própria e alinhadas à direita no desktop. O chevron foi removido por decisão de revisão e não deve ser reintroduzido nesta etapa.

## Adaptação responsiva

Grid mantém número/card no desktop; abaixo de 640px a numeração passa para uma linha acima do card, reduzindo espaços e permitindo quebra natural. Cards não têm altura fixa. Esta adaptação mobile é decisão técnica, pois o JSON fornecido é desktop.

## Pendência

Ainda falta a captura original do frame para comparação visual; não foi feita nova chamada ao MCP.

## Diagnóstico de renderização — 05/11/2026

`http://127.0.0.1:8000/` estava servindo uma cópia antiga; a confirmação foi feita em `http://127.0.0.1:8001/`, apontado explicitamente para `C:\Repos\gabisou.github.io\dist`. Em 1920 CSS px, os estilos computados confirmaram container x112/1681px, lista x121/1663px, número 72×74px e card x246/1538×217.98px. O fluxo vertical, tipografia, cores, tags e raios estavam efetivos; o chevron posteriormente foi removido por decisão de revisão.

Em 390px, as três linhas ocuparam 335px cada e `scrollWidth` ficou em 375px, sem transbordamento horizontal. A comparação visual direta com a captura Figma continua pendente.

30/10/2026. Referência: [02-services-desktop, 1:417](https://www.figma.com/design/XYP2AAZXyTlLTNvY2OphZX/GABiSOU-Site?node-id=1-417), 1920×1080. A implementação inferida existente não é referência aprovada; Mirai e versão anterior do site não definem o acabamento desta seção.

## Estrutura confirmada por Gabriel

- Introdução3:43: eyebrow e título exatos do Figma, alinhados à esquerda, início próximo de112px no desktop.
- Lista3:42: websites3:39, systems3:40 e automation3:41, três linhas empilhadas; número fora da superfície, à esquerda do card.
- Dentro de cada card: título → descrição → tags em outra linha abaixo da descrição. Grupo de tags à direita no desktop, nunca em coluna lateral ao texto.
- Cards internos aproximadamente1530×219px e gap vertical32px são referências, não caixas de tamanho fixo. Manter #solucoes e altura pelo conteúdo; header aprovado não deve mudar para reproduzir coordenadas globais do frame.

## Insumo ausente e tentativa executada

Não foi encontrada extração completa/captura original de Serviços no cache documental local. O contexto MCP do hero não contém o acabamento desta seção.

Skill figma-design-to-code lida. Uma chamada a get_design_context para1:417, com screenshot incluído, retornou: “You've reached the Figma MCP tool call limit on the Starter plan.” Nenhum contexto ou screenshot recebido. Não foram repetidas chamadas nem usadas outras ferramentas para contornar a quota.

Para retomar, é necessário **contexto textual completo das propriedades + captura do frame1:417**: textos exatos da introdução/cards/tags/numeração; fundos, cores e bordas; famílias/pesos/tamanhos/entrelinhas; raios, padding, gaps e alinhamentos; ícones e eventuais estados documentados. Metadata de posições/nomes sozinha não basta. Exportação de arte não é necessária.

## Estado e próxima ação

HTML/CSS preservados até obter a referência. A versão inferida ainda tem tags em coluna lateral no desktop, divergência conhecida; sua correção e a substituição dos textos/valores inferidos aguardam o insumo acima. Inferências antigas de cores/raios/fontes não estão autorizadas como design final.

Depois da coleta completa: ajustar um card, comparar com o frame e só então replicar aos outros dois. Distinguir valores extraídos de adaptações responsivas; não declarar fidelidade sem comparação renderizada. Header, hero, Projetos e demais seções permanecem fora desta correção. Sem push/publicação.
