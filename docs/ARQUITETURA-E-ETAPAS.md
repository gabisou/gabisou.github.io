# Arquitetura e entregas por etapa — GABiSOU

Registro de coordenação em 28/10/2026. Substitui o handoff anterior que reunia cabeçalho e abertura. Estado: tarefa da etapa 1 preparada para Gabriel encaminhar à executora B; início da execução ainda não comprovado. A primeira etapa de implementação será somente o header. Gabriel confirmou botão Menu no mobile e seção Projetos obrigatória no lançamento. Diretriz de layout incorporada em seguida: Grid como primeira opção estrutural, Flexbox nos grupos adequados e adaptação dos componentes aos pais nos dois eixos.

## Base verificada e objetivo

Repositório `gabisou/gabisou.github.io`, branch `codex/figma-redesign`, commit de partida desta atualização documental `eecd599fcb2dfb742bdb87e4fffc548e658b22a5`. Código atual: HTML/CSS estático em dist; scripts Python de verificação/release. O redesign ainda não foi implementado. Figma acessível, header/hero extraídos, referências e assets versionados. Só existe a página desktop no arquivo inspecionado.

Objetivo: explicar a oferta, demonstrar autoria real e facilitar contato. Figma aprovado orienta o visual; o código existente orienta a integração. Entrega por etapa significa uma parte integrada à prévia e verificada, não publicação automática de cada parte.

## Arquitetura e stack recomendadas

| Tema | Decisão para a primeira versão | Motivo/limite |
| --- | --- | --- |
| Arquitetura | Página única, com header, main, seções e footer semânticos; navegação por âncoras | Corresponde ao escopo institucional atual. O header repetido nos frames aparece uma única vez no DOM. |
| HTML | Conteúdo diretamente no HTML, organizado por seção | Facilita revisão de conteúdo e funciona sem renderização JavaScript. |
| CSS | CSS nativo; Grid como primeira opção estrutural, Flexbox para grupos lineares; variáveis para cores, fontes, espaçamentos, raios e limites | Diretriz de Gabriel. Componentes se adaptam aos pais. Usar valores extraídos do Figma; não impor uma escala que altere o design. |
| Organização CSS | Manter styles.css por enquanto, com blocos legíveis por componente; seletores limitados à seção | Sem reorganização completa antes do header. Regras novas não devem vazar às áreas ainda antigas. |
| JavaScript | JavaScript nativo somente quando o comportamento exigir; arquivo local carregado com defer | Não proibir JS por princípio. Conteúdo e navegação devem ter alternativa funcional se ele falhar. |
| Componentes | Contratos de marcação, estilos e estados para header, botões, cards e disclosures | Não criar biblioteca/framework de componentes antecipadamente. Extrair padrões quando o segundo uso real aparecer. |
| Bibliotecas | Nenhuma biblioteca de UI, ícones ou animação necessária até aqui | Preferir assets exatos do Figma e controles HTML adequados. |
| Build/runtime | Publicação de arquivos estáticos; Python apenas para ferramentas locais | Sem runtime Python/Node no servidor, npm, bundler ou backend exigido pelo site atual. |
| Conteúdo/contato | Texto no repositório e links para canais confirmados | Formulário, CMS, autenticação e banco não fazem parte do escopo confirmado. |
| Publicação | Reaproveitar hospedagem existente quando identificada | Domínio, deploy e rollback serão conferidos antes do lançamento; sem migração ou compra antecipada. |

A filosofia de layout abaixo é uma diretriz expressa de Gabriel. As demais escolhas de stack continuam sendo a recomendação técnica de trabalho para o escopo conhecido. Reavaliar gerador estático/framework somente se surgirem páginas ou interações que justifiquem o custo. Não há necessidade demonstrada de comparar/migrar stack nesta rodada.

## Filosofia de layout adotada

Origem: diretriz fornecida por Gabriel em 28/10/2026, aplicável a propostas, implementação e revisão. O Figma continua sendo a referência visual. As dimensões e posições extraídas orientam a fidelidade na resolução de referência; a estrutura precisa também acomodar outros tamanhos, conteúdo e ampliação.

1. **Hierarquia de fora para dentro.** Partir de container → regiões → células/grupos → componentes → conteúdo. Pais distribuem espaço; filhos o utilizam conforme sua função. Para cada região, explicar separadamente largura e altura: preencher espaço disponível, acompanhar conteúdo ou preservar proporção. Não aplicar 100% indiscriminadamente.
2. **Grid primeiro na estrutura.** Usá-lo para regiões, alinhamentos compartilhados, linhas e colunas. Flexbox é adequado para grupos predominantemente lineares, como ações ou ícone com texto. Combinar quando simplificar; escolher pelo comportamento, sem obrigar toda caixa a ser Grid.
3. **Relações e limites.** Preferir dimensionamento pelo conteúdo, frações do espaço, mínimos, máximos e proporções a dimensões rígidas escolhidas só para copiar uma captura. Considerar fr, minmax(), min(), max(), clamp() e aspect-ratio quando úteis, sem obrigação de usar todos. Bordas, ícones, espaçamentos e limites de leitura/interação podem ter medidas definidas com função clara. Porcentagens em tudo também não garantem adaptação.
4. **Caixa e conteúdo são distintos.** Campos podem ocupar a coluna sem esticar letras; imagens e ícones preservam proporção dentro da área disponível. “Scale to fit” significa ajuste proporcional com limites de uso. object-fit: contain pode servir a imagens/mídias, não a formulários inteiros; transform: scale() não substitui reorganizar o layout.
5. **Origem da altura.** Nesta página institucional, o padrão é altura pelo conteúdo e rolagem do documento. Não transformar frames de 1080 px em seções com altura fixa ou exigir que tudo caiba numa tela. Se houver uma região realmente delimitada em altura, explicar de onde a altura vem e o que cresce, encolhe ou rola. height: 100% depende de referência resolvível; unidades de container exigem identificar o container e os eixos de referência.
6. **Falta de espaço explícita.** Antes de reduzir elementos, revisar estrutura, mínimos do conteúdo, espaços e restrições dos pais. minmax(0, 1fr), min-width: 0 e min-height: 0 podem permitir encolhimento quando apropriado, mas ainda é necessário tratar o conteúdo excedente. Reorganizar colunas, quebrar linhas ou rolar a região adequada. Determinar breakpoints onde o conteúdo deixa de funcionar, sem limitar a decisão a categorias de dispositivo. Não esconder conteúdo essencial com overflow: hidden nem reduzir indefinidamente fontes/botões. O recorte documentado da arte decorativa não autoriza cortar texto, controles ou foco.
7. **Usabilidade preservada.** Manter legibilidade, proporções, ações alcançáveis, teclado e foco visível; respeitar zoom e ampliação de texto. Em telas estreitas ou baixas, mudar a composição ou permitir rolagem antes de comprimir o uso. Não exigir visibilidade simultânea de todo o conteúdo.
8. **Demonstrar e verificar.** Antes de editar, examinar componentes/padrões existentes. Toda proposta ou retorno deve dizer: container responsável; determinação de largura/altura; o que cresce, encolhe ou preserva proporção; limites; resposta à falta de espaço. Validar com conteúdo real, textos longos, diferentes larguras e alturas e redimensionamento contínuo. Registrar o que não foi testado. Consultar documentação oficial atual e citar a fonte efetivamente lida quando houver dúvida de sintaxe, suporte ou comportamento.

Contrato curto a incluir na tarefa de cada etapa:

> Container responsável: …; largura: …; altura e sua origem: …; crescimento/encolhimento/proporção: …; limites: …; falta de espaço: …; evidências e pendências: ….

Este contrato não exige uma nova biblioteca, container queries ou infraestrutura. Usar esses recursos apenas quando o comportamento da seção justificar.

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
- Desktop de referência: 1920 px de largura e header observado com 125 px; fundo #F7F7F0, borda #282836, logo 260 × 77 e navegação Inter 22 px. Usar a geometria completa de DESIGN-HERO.md. Os 125 px são alvo de comparação nesse contexto, não altura fixa para todas as situações.
- Comportamento base: um header no fluxo da página, sem fixação ou animação de scroll não especificadas.
- Contrato de layout proposto: header ocupa a largura da página; sua grade interna organiza marca e navegação/ações. Limites, margens e intervalos devem reproduzir os alinhamentos do frame, inclusive o espaço livre à direita; não esticar automaticamente a navegação até a borda. A altura acompanha conteúdo e espaçamentos, podendo crescer com quebra de texto, zoom ou menu aberto.
- A marca cabe em sua célula preservando a proporção 260:77 e um limite coerente com a referência; textos e botões mantêm dimensões de uso. A lista de navegação pode usar Flexbox por ser linear. A transição para Menu ocorre quando os itens, com a fonte real, deixam de caber de forma utilizável; o breakpoint exato exige verificação.
- Na adaptação compacta, a grade organiza marca e botão Menu na primeira linha; a navegação aberta ocupa a linha seguinte, com largura disponível e altura pelo conteúdo. Rótulos podem quebrar. Em telas baixas, a página rola para alcançar todos os links; não prender o menu a uma altura que corte seu conteúdo. Preservar uma ordem de leitura/foco coerente.
- Contato do header aponta para #contato; esta etapa não depende de escolher WhatsApp para o CTA do hero.
- Escolha confirmada por Gabriel para mobile: botão “Menu” que expande uma lista de links no fluxo, sem drawer/modal. Implementar botão nativo com aria-expanded/aria-controls, Tab/Enter/Espaço, Escape para fechar e devolver foco; fechar ao selecionar âncora. Alternativa visível sem JS. Este comportamento substitui a sugestão anterior de segunda faixa sempre visível. O desenho mobile continua sendo adaptação, pois não há frame da designer.
- Projetos: obrigatório no lançamento por escolha de Gabriel; manter a intenção de navegação no header. Enquanto a seção real não existir, identificar o item como pendente na prévia em vez de criar âncora quebrada. Etapa 4 deverá entregar conteúdo real autorizado; não há autorização para omitir a seção no lançamento.
- Escopo de suporte: tokens/fonte necessários, CSS do header, JS do menu expansível já escolhido e ajuste direcionado dos checks.
- Evidências: comparar a região do header em 1920 × 1080; conferir reflow nas larguras 1440/768/390/320 px e redimensionamento contínuo, incluindo a transição do Menu. Incluir uma janela baixa (por exemplo 1440 × 600), paisagem mobile (por exemplo 844 × 390), menu aberto/fechado, texto ampliado a 200% e zoom do navegador a 200%/400%, registrando viewport/zoom efetivos. Conferir texto longo temporário sem alterar o conteúdo final, teclado/foco, links, carregamento do logo/fonte, console e ausência de transbordamento horizontal. Reflow a 320 CSS px e teste de zoom não equivalem a uma auditoria completa de acessibilidade. Capturas devem cobrir os estados representativos, sem exigir imagem de cada tamanho intermediário.
- Nenhuma comparação visual do código ocorreu ainda. B não comprovou que seu Chrome remoto chega ao servidor; C é a alternativa proposta, com navegador local ainda por validar.

## Critério para encerrar cada etapa

1. Componente implementado e integrado à prévia, com desktop e mobile e contrato de largura/altura, limites e falta de espaço explicado.
2. Checks pertinentes aprovados, interações verificadas e adaptação exercitada em diferentes larguras/alturas, redimensionamento contínuo, texto longo, ampliação de texto, zoom e teclado.
3. Captura identificada por commit e viewport comparada à referência Figma; correções materiais concluídas.
4. Mobile identificado como adaptação quando não houver frame aprovado.
5. Diff/commit revisável, pendências explícitas e registro curto em CONTINUIDADE/VERIFICACAO.

“Implementado” e “verificado visualmente” são estados distintos. Só a segunda condição permite encerrar a etapa. Resolver uma vez o caminho de visualização para repetir esse ciclo nas próximas entregas.

## Pausa e revisão entre etapas

Cada unidade revisável (header, hero e demais seções da sequência) segue este ciclo:

1. B implementa somente o escopo atribuído, executa os checks pertinentes e prepara código/preview identificado pelo commit.
2. A renderização é comparada ao Figma e verificada nos estados e tamanhos do contrato. B faz isso se tiver navegador funcional; se o impedimento conhecido persistir, C recebe uma tarefa de validação do mesmo commit no Windows. C não implementa a próxima seção.
3. A coordenação confere evidências, escopo e limitações; Gabriel recebe a prévia/capturas para validar o resultado visual. Logo, links, contato e menu aberto/fechado fazem parte da revisão do header.
4. Havendo problemas, corrigir e rever a mesma etapa. Depois da revisão técnica/visual e do aceite de Gabriel, a coordenação prepara a próxima tarefa. B não avança automaticamente ao hero.

Se faltar renderização, a entrega permanece “implementada; validação visual pendente”. Não fechar a etapa só com HTTP 200/check estático. Não é necessário deploy público para revisão local; o caminho de visualização deve ser comprovado antes de encerrar a primeira etapa.

Situação de publicação verificada em 28/10/2026: GitHub Pages desativado e zero execuções de Actions na branch de redesign. Nenhum deploy do redesign foi realizado nesta coordenação. Hospedagem/fluxo do domínio histórico ainda não identificados; esses sinais não comprovam ausência de uma hospedagem externa. Nenhum serviço novo será configurado nesta tarefa.

## Decisões abertas e momento de resolução

| Decisão | Quando importa | Responsável |
| --- | --- | --- |
| Desenho fino do menu mobile já escolhido | Etapa 1 | Coordenação/executora; consultar Carol se houver impacto visual material |
| Materiais reais para Projetos, já obrigatório | Etapa 4, necessariamente antes do lançamento | Gabriel/Carol |
| Caminho comprovado de captura/renderização | Antes de encerrar etapa 1 | Coordenação e executora do ambiente adequado |
| WhatsApp comercial | Etapa 2/contato | Gabriel |
| Conteúdo e assets das outras seções | Ao preparar cada etapa | Coordenação; Gabriel/Carol para fatos/autorizações |
| Hospedagem e publicação | Antes do lançamento | Gabriel + coordenação |

Próxima ação: Gabriel encaminhar o handoff da etapa 1 à executora B. A coordenação recebe o retorno para revisar o header; se faltar renderização, prepara a tarefa delimitada de C a partir do commit entregue. Usar a filosofia de layout e o contrato acima, sem reabrir inventário geral nem repetir tentativas de localhost sem nova evidência.

## Referências técnicas consultadas
- [W3C: navegação expansível](https://www.w3.org/WAI/ARIA/apg/patterns/disclosure/examples/disclosure-navigation/) — padrão de comportamento e semântica, não código pronto para copiar sem testes.
- [MDN: variáveis CSS](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascading_variables/Using_custom_properties).
- [MDN: details/summary](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/details).
- [MDN: grid-template-columns](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/grid-template-columns) — dimensionamento de trilhas, mínimos e frações; consultado em 28/10/2026.
- [MDN: height](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/height) — referência das alturas percentuais; consultado em 28/10/2026.
- [W3C: reflow](https://www.w3.org/WAI/WCAG22/Understanding/reflow.html) — reorganização com ampliação e largura equivalente de 320 CSS px; consultado em 28/10/2026.
