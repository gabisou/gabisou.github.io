# Arquitetura e entregas por etapa — GABiSOU

Registro de coordenação em 28/10/2026. Substitui o handoff anterior que reunia cabeçalho e abertura. Estado: organização; nenhuma tarefa nova foi enviada às executoras. A primeira etapa de implementação será somente o header. Gabriel escolheu nesta rodada: botão Menu no mobile e seção Projetos obrigatória no lançamento.

## Base verificada e objetivo

Repositório `gabisou/gabisou.github.io`, branch `codex/figma-redesign`, commit inspecionado `68bd0d5ba781531d82f45fa7fc6ed821f4776a57`. Código atual: HTML/CSS estático em dist; scripts Python de verificação/release. O redesign ainda não foi implementado. Figma acessível, header/hero extraídos, referências e assets versionados. Só existe a página desktop no arquivo inspecionado.

Objetivo: explicar a oferta, demonstrar autoria real e facilitar contato. Figma aprovado orienta o visual; o código existente orienta a integração. Entrega por etapa significa uma parte integrada à prévia e verificada, não publicação automática de cada parte.

## Arquitetura e stack recomendadas

| Tema | Decisão para a primeira versão | Motivo/limite |
| --- | --- | --- |
| Arquitetura | Página única, com header, main, seções e footer semânticos; navegação por âncoras | Corresponde ao escopo institucional atual. O header repetido nos frames aparece uma única vez no DOM. |
| HTML | Conteúdo diretamente no HTML, organizado por seção | Facilita revisão de conteúdo e funciona sem renderização JavaScript. |
| CSS | CSS nativo, Flexbox/Grid; variáveis para cores, fontes, espaçamentos, raios e larguras | Usar valores extraídos do Figma; não impor uma escala que altere o design. |
| Organização CSS | Manter styles.css por enquanto, com blocos legíveis por componente; seletores limitados à seção | Sem reorganização completa antes do header. Regras novas não devem vazar às áreas ainda antigas. |
| JavaScript | JavaScript nativo somente quando o comportamento exigir; arquivo local carregado com defer | Não proibir JS por princípio. Conteúdo e navegação devem ter alternativa funcional se ele falhar. |
| Componentes | Contratos de marcação, estilos e estados para header, botões, cards e disclosures | Não criar biblioteca/framework de componentes antecipadamente. Extrair padrões quando o segundo uso real aparecer. |
| Bibliotecas | Nenhuma biblioteca de UI, ícones ou animação necessária até aqui | Preferir assets exatos do Figma e controles HTML adequados. |
| Build/runtime | Publicação de arquivos estáticos; Python apenas para ferramentas locais | Sem runtime Python/Node no servidor, npm, bundler ou backend exigido pelo site atual. |
| Conteúdo/contato | Texto no repositório e links para canais confirmados | Formulário, CMS, autenticação e banco não fazem parte do escopo confirmado. |
| Publicação | Reaproveitar hospedagem existente quando identificada | Domínio, deploy e rollback serão conferidos antes do lançamento; sem migração ou compra antecipada. |

Esta arquitetura é a recomendação técnica de trabalho para o escopo conhecido, não uma preferência atribuída a Gabriel. Reavaliar gerador estático/framework somente se surgirem páginas ou interações que justifiquem o custo. Não há necessidade demonstrada de comparar/migrar stack nesta rodada.

## Engenharia para migração incremental

- `dist/index.html` e `dist/styles.css` continuam sendo fontes editáveis; `build/` é saída de release. Não renomear diretórios por convenção agora.
- O CSS atual tem variáveis globais, regras genéricas e media queries compartilhadas. Trocar valores globais pode redesenhar seções fora do escopo. Introduzir tokens distintos do redesign e aplicá-los nos componentes migrados.
- O body existente já cita Inter sem carregar a fonte. Registrar a nova fonte com família própria e aplicá-la primeiro ao header evita alterar silenciosamente a tipografia do restante.
- Na etapa do header, modificar somente suas regras e as dependências compartilhadas indispensáveis. Não acumular overrides duplicados ao fim do CSS; manter uma definição compreensível.
- Conteúdo, apresentação e comportamento têm responsabilidades separadas: HTML, CSS e JS local quando necessário. Nada de gerar conteúdo principal via JavaScript.
- Aproveitar semântica nativa. FAQ pode usar details/summary se compatível com seus estados aprovados. Navegação comum deve usar nav/lista/links, sem o papel ARIA menu de aplicativos.
- Manter IDs das seções existentes. Tratar links para seções futuras explicitamente na prévia; produção não pode conter âncoras quebradas ou cases fictícios.
- Uma executora altera os arquivos de implementação por vez. Registrar commit de partida e saída; cada etapa deve ter diff delimitado e revisão própria. Correções continuam pertencendo à etapa atual.
- A migração pode deixar a prévia temporariamente com header novo e conteúdo antigo. Não confundir essa prévia de transição com a entrega final.
- O check atual exige alt não vazio em toda imagem e rejeita qualquer script src, até local. Evoluir essas regras na etapa em que houver uso legítimo: imagem decorativa com alt vazio, JS local existente e destino WhatsApp confirmado. Preservar a intenção dos checks e não apagar validações só para obter PASS.

## Biblioteca de assets

Será um catálogo de arquivos locais e de sua procedência, não uma dependência externa. A extração detalhada atual está em DESIGN-HERO.md.

| Arquivo existente | Uso | Procedência/estado |
| --- | --- | --- |
| dist/assets/figma/gabisou-wordmark.png | Marca do header | Nó 1:210; PNG 260 × 77. Verificar nitidez nas dimensões usadas. |
| dist/assets/figma/hero-artwork.png | Arte decorativa da etapa 2 | Nó 3:25; PNG 935 × 907, efeito estático incorporado. |
| dist/assets/fonts/InterVariable.woff2 | Tipografia | Inter oficial v4.1; fonte normal variável. Comparar métricas com Figma. |
| dist/assets/fonts/Inter-LICENSE.txt | Licença da fonte | Manter junto à distribuição. |
| docs/design/hero-desktop-1920.png | Referência de QA | Frame 1:200; não usar como imagem da página. |
| dist/assets/logo.png e favicon.svg | Assets anteriores | Preservar usos fora do escopo; revisar adoção/substituição na etapa pertinente. |

Para cada asset futuro, registrar arquivo, seção, nó/origem, dimensões, licença ou autorização e estado (final/placeholder). Preferir SVG quando houver original vetorial aprovado; preservar o raster quando for o original adequado. Não converter/desenhar logos por aproximação. Novas categorias de pastas surgem conforme necessário. Sem URLs temporárias, fontes em CDN ou fotos inventadas. Otimização de imagens deve preservar o visual e ser verificada; não transformar tudo antecipadamente.

## Sequência de entregas

A ordem abaixo acompanha os frames existentes e separa o header. Uma pendência de conteúdo pode adiar uma etapa, sem alterar silenciosamente a composição aprovada.

| Etapa | Entrega delimitada | Referência Figma | Condição específica |
| --- | --- | --- | --- |
| 1 | Header: marca, navegação e contato | 3:4, dentro de 1:200 | Desktop, proposta mobile, links e foco. Não implementar hero junto. |
| 2 | Hero: título, apoio, CTA e arte | 1:200, excluindo header já concluído | Destino do WhatsApp confirmado para funcionalidade final. |
| 3 | Serviços | 1:417 | Definir se as setas abrem conteúdo; não inferir apenas pela forma do ícone. |
| 4 | Projetos | 1:470 | Obrigatória no lançamento por escolha de Gabriel. Conteúdo real autorizado é requisito de publicação; placeholders só na prévia. |
| 5 | Como trabalhamos | 1:513 | Confirmar conteúdo completo e assets ao extrair a seção. |
| 6 | Quem somos | 1:552 | Fotos, apresentações e links reais autorizados. |
| 7 | FAQ | 1:582 | Respostas confirmadas e estados aberto/fechado funcionais. |
| 8 | Contato | 1:623 | Canal e destinatário corretos; nenhuma promessa de formulário funcional sem implementação. |
| 9 | Footer | 1:640 | Links reais, marca e retorno ao topo. |
| 10 | Integração e lançamento | Página completa | QA global, conteúdo final, SEO, hospedagem, rollback e autorização de publicação. |

Não extrair todos os frames agora. Preparar apenas a etapa próxima, reaproveitando as referências já obtidas.

## Contrato preliminar da etapa 1 — header

- Entradas prontas: nó 3:4, referência visual desktop, wordmark, Inter, links/IDs das seções existentes.
- Desktop de referência: 1920 px de largura e header de 125 px; fundo #F7F7F0, borda #282836, logo 260 × 77 e navegação Inter 22 px. Usar a geometria completa de DESIGN-HERO.md.
- Comportamento base: um header no fluxo da página, sem fixação ou animação de scroll não especificadas.
- Contato do header aponta para #contato; esta etapa não depende de escolher WhatsApp para o CTA do hero.
- Escolha confirmada por Gabriel para mobile: botão “Menu” que expande uma lista de links no fluxo, sem drawer/modal. Implementar botão nativo com aria-expanded/aria-controls, Tab/Enter/Espaço, Escape para fechar e devolver foco; fechar ao selecionar âncora. Alternativa visível sem JS. Este comportamento substitui a sugestão anterior de segunda faixa sempre visível. O desenho mobile continua sendo adaptação, pois não há frame da designer.
- Projetos: obrigatório no lançamento por escolha de Gabriel; manter a intenção de navegação no header. Enquanto a seção real não existir, identificar o item como pendente na prévia em vez de criar âncora quebrada. Etapa 4 deverá entregar conteúdo real autorizado; não há autorização para omitir a seção no lançamento.
- Escopo de suporte: tokens/fonte necessários, CSS do header e, se o menu expansível for adotado, seu JS e ajuste direcionado dos checks.
- Evidências: comparação da região do header no viewport 1920 × 1080, reflow a 1440/768/390/320 px, teclado/foco, links, carregamento do logo/fonte, console e ausência de overflow.
- Nenhuma comparação visual do código ocorreu ainda. B não comprovou que seu Chrome remoto chega ao servidor; C é a alternativa proposta, com navegador local ainda por validar.

## Critério para encerrar cada etapa

1. Componente implementado e integrado à prévia, com desktop e mobile.
2. Checks pertinentes aprovados e interações do escopo verificadas.
3. Captura identificada por commit e viewport comparada à referência Figma; correções materiais concluídas.
4. Mobile identificado como adaptação quando não houver frame aprovado.
5. Diff/commit revisável, pendências explícitas e registro curto em CONTINUIDADE/VERIFICACAO.

“Implementado” e “verificado visualmente” são estados distintos. Só a segunda condição permite encerrar a etapa. Resolver uma vez o caminho de visualização para repetir esse ciclo nas próximas entregas.

## Decisões abertas e momento de resolução

| Decisão | Quando importa | Responsável |
| --- | --- | --- |
| Desenho fino do menu mobile já escolhido | Etapa 1 | Coordenação/executora; consultar Carol se houver impacto visual material |
| Materiais reais para Projetos, já obrigatório | Etapa 4, necessariamente antes do lançamento | Gabriel/Carol |
| Caminho comprovado de captura/renderização | Antes de encerrar etapa 1 | Coordenação e executora do ambiente adequado |
| WhatsApp comercial | Etapa 2/contato | Gabriel |
| Conteúdo e assets das outras seções | Ao preparar cada etapa | Coordenação; Gabriel/Carol para fatos/autorizações |
| Hospedagem e publicação | Antes do lançamento | Gabriel + coordenação |

Próxima ação da coordenação: usar o contrato do header e as escolhas registradas para preparar, quando retomarmos a execução, uma tarefa exclusiva da etapa 1. Confirmar o caminho de conferência visual sem reabrir inventário geral. Nenhum prompt novo de execução integra esta rodada.

## Referências técnicas consultadas
- [W3C: navegação expansível](https://www.w3.org/WAI/ARIA/apg/patterns/disclosure/examples/disclosure-navigation/) — padrão de comportamento e semântica, não código pronto para copiar sem testes.
- [MDN: variáveis CSS](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascading_variables/Using_custom_properties).
- [MDN: details/summary](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/details).
