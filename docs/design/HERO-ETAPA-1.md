# Hero — coleta de 30/10/2026

Referência: https://www.figma.com/design/XYP2AAZXyTlLTNvY2OphZX/GABiSOU-Site?node-id=1-200
Frame desktop 1920×1080. Texto 3:24; ilustração 3:25. O risco sobre AI FIRST (13:12) está FORA do grupo da ilustração e precisa acompanhar sua exportação.

Captura obtida pelo contexto: 1024×576, reduzida proporcionalmente; referência visual, nunca asset da página. Contexto MCP anexado para consulta seletiva, não para executar literalmente. React/Tailwind/shader runtime retornados não definem a stack. Preservar HTML/CSS/JS existentes.

## Verificado

- Páginas: Website — Desktop; 02 — Asset library; 03 — References. Nenhuma página mobile identificada; não há hero mobile na página desktop consultada.
- Fundo do hero #F5F7F0. Inter local reutilizável, sem afetar a fonte do restante da página.
- Título em duas partes: “Desenvolvimento de soluções digitais” (40px, peso500, preto) e “para a realidade da sua empresa.” (40px, peso700, #4A36EB). Caixa desktop x84 y296, 721×96.
- Descrição: “A GABiSOU transforma necessidades do seu negócio em soluções digitais, com execução técnica e conversa próxima.” Inter24px/peso400. Caixa x85 y482, 909×58.
- CTA “Entre em contato”: x85 y598, 303×99; fundo #4A36EB, texto branco32px/peso500, raio18px.
- Auxiliar: “Por whatsapp, direto com a equipe de humanos”, 16px/peso400; x85 y713, 361×19.
- Gaps de referência: título→descrição90px; descrição→CTA58px; CTA→auxiliar16px. Usar esses valores como limites desktop, flexibilizar com o espaço disponível.
- Header no Figma ainda125px; preservar header aprovado de aproximadamente80px e ordem atual do menu.
- Ilustração inclui efeito de lente estático, painéis rotacionados, ícones e monograma. A exportação oficial foi bloqueada pela quota Starter. Não repetir chamadas nem instalar runtime para contornar a exportação.
- Na cópia remota consultada existe e-mail, mas não foi localizado destino WhatsApp. A C deve conferir também sua cópia local atual.

## Decisões para implementação parcial

1. Escopo agora: bloco de texto, CTA e estrutura responsiva do hero. Ilustração pendente de exportação, sem inventar substituta.
2. Grid para as regiões texto/arte, altura pelo conteúdo. No desktop amplo, reproduzir margem esquerda84–85px e limites acima; usar referências relativas ao fim do header: título171px abaixo. Não restaurar o header antigo para obter o y296 da captura.
3. Em telas menores, reduzir espaçamentos antes de comprimir texto. Empilhar texto e arte quando a composição deixar de caber. Breakpoint do hero é independente do header.
4. No mobile, texto primeiro, ação depois e arte abaixo; fonte do título com mínimo28px, corpo18px, botão legível com alvo mínimo44px. São decisões inferidas, sujeitas à revisão humana.
5. CTA usa WhatsApp apenas se houver destino confirmado. Caso contrário, usar #contato e auxiliar provisório “Fale diretamente com a equipe.”, registrado como diferença temporária em relação ao Figma.
6. Remover a ilustração antiga do hero desta nova composição; reservar sua região com indicação discreta “Ilustração em preparação” somente na prévia. Não publicar como entrega final.
7. Próxima parte: importar asset estático oficial da ilustração, com efeito e risco de AI FIRST; avaliar composição junto ao texto. Não usar screenshot do hero como imagem da página.

## Handoff para C

DESTINATÁRIA: C, no Windows, modo econômico.

OBJETIVO: implementar apenas texto/CTA e estrutura do hero conforme este documento, sem avançar às demais seções.

CONTEXTO: C:\Repos\gabisou.github.io; branch codex/figma-redesign; último HEAD informado eaa38db79d388901e273abb4d54ad6fa8703158d. Confirmar estado real. Ler AGENTS.md e continuidade pertinente. Há trabalho local anterior que deve ser preservado.

ESCOPO: dist/index.html, regras de hero em dist/styles.css, documentação pertinente. Preservar header aprovado, header.js, Projetos e outras seções. Não instalar ferramentas nem alterar stack.

EXECUÇÃO: guardar estes três documentos em docs/design sem sobrescrever outros. Antes de editar, conferir diff e criar commit local de checkpoint somente dos arquivos de projeto revisados; discriminar alterações anteriores, não incluir segredos, temporários ou ZIPs. Não fazer push. Inspecionar componentes existentes; executar as decisões acima com Grid estrutural, Flex para agrupamentos locais, dimensões por conteúdo e limites, sem escala artificial da página ou overflow escondendo textos. O contexto MCP é referência de valores: não copiar posições absolutas globais, o header nele contido ou seus imports de React/shaders. Não reler todo o Figma.

CONCLUÍDO QUANDO: texto e CTA correspondem à referência, preservadas as exceções documentadas. Comparação focada em1920px e390px; conferir uma largura intermediária por redimensionamento, quebra de texto, foco e destino do botão. Reutilizar servidor existente e recurso de captura em segundo plano apenas se disponível, sem controlar mouse/teclado do PC. Se indisponível, entregar diff e pendência visual objetiva. Executar python -X utf8 scripts/check.py e git diff --check uma vez. Não repetir suítes nem testes de header.js sem modificações.

RETORNO: HEAD/commit do checkpoint, mudanças desta etapa, checks, capturas se disponíveis, link local e pendências ilustração/WhatsApp. Não declarar hero completo. Parar para revisão humana antes de importar arte ou iniciar Serviços.
