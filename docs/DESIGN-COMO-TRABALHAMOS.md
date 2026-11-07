# Como trabalhamos — referência 04-process-desktop

Fonte: JSON fornecido do frame `04-process-desktop`, nó `1:513`, 1920×1080. A composição implementada usa fundo contínuo `#F7F7F0`, introdução e quatro etapas em Grid; as ilustrações raster/vetorial não estão disponíveis nos assets locais e os espaços foram reservados sem imagens substitutas.

## Conteúdo e tipografia

Rótulo `Como trabalhamos`; título `Do primeiro contato à solução em uso.`. Etapas: ENTENDER, DEFINIR, DESENVOLVER e ENTREGAR com os textos fornecidos. Inter local registrada como `Gabisou Header Inter`; rótulo 26/31.4659 peso300, título 40/48.4091 peso500, número 96/116.1818 peso300 roxo `#4A36EB`, títulos 40/48.4091 peso300 e descrições 24/29.0455 peso400, todos com letter-spacing normal.

## Geometria e responsividade

Desktop usa container próprio de referência 1920px, Grid de quatro trilhas de 420px com os deslocamentos horizontais/verticais do JSON. Cada etapa tem número com traços decorativos internos, descrição em fluxo e reserva de mídia 208×135px. Abaixo de 1450px, as etapas passam a duas colunas; abaixo de 700px, uma coluna. Esses breakpoints são decisões de encaixe, pois o JSON é desktop.

## Pendências

Exportação/localização das quatro ilustrações e comparação visual direta com o frame permanecem pendentes. Nenhuma interação ou animação foi criada.

## FAQ integrado

O bloco `Dúvidas frequentes.` foi integrado abaixo das quatro etapas, dentro da mesma section `#como-trabalhamos`. O texto `Antes de começar` foi removido; as cinco perguntas permanecem fechadas e não focáveis, com sinais de mais decorativos. Desktop usa Grid de introdução/lista (462px + 506px + 711px) e desalinhamento vertical de 98px na introdução. A junção usa 120px no desktop e 64px no mobile por decisão de integração, não por medida extraída do JSON. Em telas menores, introdução fica acima da lista e os divisores acompanham a largura disponível.
