# Projetos — estrutura autorizada com placeholders

## Decisão e escopo

Após comprovar o setup local, Gabriel autorizou implementar Projetos mesmo sem conteúdo final, como parte do próprio site. Remover “Pendente na prévia” do header: Projetos será um link normal para `#projetos`, com destino existente. Antecipar a estrutura dos cards; hero continua fora do escopo. Header e Projetos têm evidências e aceite visual separados.

Placeholders de título, imagem, resumo e tags não são cases reais. Reaproveitar exatamente os campos neutros do Figma, sem inventar clientes, nomes de projetos realizados, resultados ou fotografias. A falta desses materiais não bloqueia a implementação. Isto não autoriza publicação, merge ou novas funcionalidades.

## Referência efetivamente lida

- Arquivo: https://www.figma.com/design/XYP2AAZXyTlLTNvY2OphZX/GABiSOU-Site?node-id=1-470
- Frame `1:470`, `03-projects-desktop`, 1920 × 1080.
- Captura: `docs/design/projects-desktop-1-470-1920.png`, PNG original 1920 × 1080; referência de comparação, nunca imagem de fundo da implementação.
- Contexto completo e captura obtidos pelo MCP oficial nesta decisão; sem editar Figma. Reutilizar esta extração.
- Componente `Cards/Project 27:318`: Title/Summary editáveis; Media/Tags são slots; sem afirmações de projetos reais.
- Lista `3:59`; rótulo da seção `1:481`; tags `Tags/Label 25:173`, tamanho Medium `25:171`; ação `Actions/Button 25:35`, Secondary/Default `25:31`.
- O header `25:55` aparece no frame como contexto compartilhado. O site continua tendo um único header; não duplicá-lo dentro de Projetos.
- Nenhum comportamento mobile está documentado nesta extração. A adaptação precisa ser registrada e validada.

## Dados explícitos do desktop

Coordenadas relativas ao frame de 1920 × 1080. São referências de comparação, não instrução para posicionar a página inteira de forma absoluta.

| Elemento | Geometria / estilo |
| --- | --- |
| Fundo | #F7F7F0 |
| Header de contexto | y 0–125; reutilizar implementação existente |
| Título “Projetos” | x 112, y 158; Inter Light 300, 26 px, preto |
| Cards | x 155 / 698 / 1248; y 251; cada caixa 517 × 561; fundo #E9EFEC; raio 22 px |
| Mídia de cada card | topo do card, 517 × 255; retângulo #7D7D7D; texto “IMG” branco, Inter Regular 400, 34 px |
| Título do card | texto “Titulo do projeto1”, igual nos três; posição interna x 7, y 15; largura 503; Inter Light 300, 26 px, preto; sobre a área de mídia |
| Resumo | “Resumo breve de projeto”; posição interna x 14, y 275; largura 489; Inter Light 300, 26 px, preto |
| Tags | duas “Palavra-chave” por card; grupo interno x 19, y 495, caixa 479 × 46; posições internas x 0 e 159 |
| Tag individual | altura de referência 46; largura pelo texto; padding horizontal 9; raio 9; fundo #C6D2CC; Inter Light 300, 20 px, texto #4A36EB |
| “Ver mais →” | x 814, y 890, caixa 288 × 73; fundo #C6D2CC; raio 18; padding horizontal 20 e vertical 10; Inter Light 300, 32 px, preto |

O contexto declara line-height normal. Conferir métricas renderizadas. O texto “IMG” fica em x 204/y 115 no primeiro slot e x 225/y 115 nos demais; não inferir alinhamento uniforme como fato do Figma. Os intervalos horizontais observados entre cards são 26 e 33 px. Caso a adaptação simplifique essas pequenas assimetrias, registrar a decisão e a diferença na comparação.

Não há imagem externa para os placeholders: o Figma usa retângulos e texto. Implementá-los em HTML/CSS, não gerar imagens ou baixar fotografias. Fonte Inter local existente suporta os pesos necessários; aplicar a família apenas aos componentes desta rodada para não alterar seções antigas.

## Contrato de implementação

- Preservar HTML/CSS/JS nativo e os arquivos existentes. Antes de editar, ler AGENTS.md, verificar branch/HEAD e alterações locais.
- Inserir `section id="projetos"` em `main`, após Serviços (`#solucoes`) e antes das seções seguintes existentes, sem reordenar ou reimplementar seu conteúdo.
- Remover o aviso e o estado desabilitado do item do header, usando `a href="#projetos"`. Preservar texto, fonte e aparência do link do Figma; verificar fechamento do Menu e âncora.
- Estrutura de seção com heading e três cards semânticos. Grid distribui cards; cada card acomoda mídia, título, resumo e tags. Flexbox é adequado ao grupo de tags. Conteúdo permanece no HTML.
- Largura: container limitado e centralizado reproduz a composição desktop; cards utilizam as colunas disponíveis. Altura: acompanha conteúdo; não impor 1080 px à seção nem 561 px a todos os estados do card.
- Mídia preserva proporção 517:255. O título sobre a mídia ocupa sua própria camada de Grid, sem esticar fontes nem posicionar toda a página por coordenadas.
- Em larguras menores, reduzir colunas quando conteúdo/mínimos exigirem; chegar a uma coluna. Tags e títulos podem quebrar. Em alturas baixas, usar rolagem do documento. Não esconder conteúdo ou foco para evitar overflow.
- Não renomear famílias globais nem criar design system, biblioteca ou framework. Reutilizar assets e padrões compatíveis; isolar estilos em seletores de Projetos.
- “Ver mais →” não tem destino/interação documentados nem projetos adicionais fornecidos. Nesta rodada, preservar seu espaço e aparência com botão nativo desabilitado, sem href fictício ou ação que não acontece. Registrar a pendência; não declarar esse comportamento final. Não inventar página, modal ou cases para torná-lo ativo.
- Não adicionar selo de prévia ou aviso de andamento ao menu. Pendências de conteúdo ficam nos campos neutros e no registro técnico.

## Verificação e pausa

1. Reexecutar `python -X utf8 scripts/check.py`, `node --check dist/header.js` e `git diff --check` após as mudanças. Quantidades de links/IDs poderão aumentar legitimamente; investigar mudanças, sem enfraquecer validações.
2. Conferir `#projetos` por mouse e teclado, inclusive Menu mobile, fechamento ao seguir a âncora, foco e ausência de destino quebrado.
3. Comparar header com sua captura vigente. Comparar Projetos com esta captura, considerando que os 125 px superiores são o header de contexto, e não conteúdo a repetir.
4. Capturas originais e metadados: SHA de base, patch aplicado, viewport CSS real, área útil, DPR, zoom e pixels do arquivo. Não ajustar CSS nem reamostrar capturas apenas para forçar dimensões iguais.
5. Usar o checklist responsivo/teclado/zoom da etapa do header; conferir também cards e tags em 1920, 1440, 768, 390 e 320 px, janela baixa e redimensionamento contínuo. Nenhuma afirmação de fidelidade mobile sem frame aprovado.
6. Sem erros relevantes de console, fonte/asset ausente ou overflow indevido nas áreas alteradas. Registrar regressões fora do escopo sem ampliar a tarefa.
7. Entregar diff completo e capturas anexáveis de header desktop, mobile aberto/fechado e Projetos desktop/mobile. Atualizar os registros locais já modificados; não os substituir pelo remoto.
8. Parar para revisão técnica e visual de Gabriel. Não avançar ao hero. Não fazer commit/push local ou deploy nesta rodada.

Modo recomendado: econômico/suficiente, reaproveitando este contrato. Maior capacidade só para lacuna material ou diagnóstico que não avance após duas tentativas fundamentadas. Não afirmar troca de modelo/esforço sem controle verificável.
