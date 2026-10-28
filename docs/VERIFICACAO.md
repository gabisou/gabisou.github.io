# Verificação — header do redesign

28/10/2026, Brasília. **Implementado; validação visual pendente.** Não houve deploy nem avanço ao hero.

## Identificação e escopo

Base técnica/documental: c5dd9ef0a9256d62f8f0887dcf05027b77189d52. Referência atual e aprovação persistidas em e7f90ff094e8ad80f134fd8c3c5fa6f924e270e1. A implementação pertence ao commit que introduz este registro; o SHA final acompanha o handoff da coordenação.

Figma aprovado: 25:55, Contato #C6D2CC. Captura vigente: docs/design/header-desktop-25-55-1920.png, 1920 × 125. O header da captura antiga hero-desktop-1920.png é histórico.

Arquivos de código verificados (blobs Git):
- dist/index.html: 7a66c74024939de4eef7e7be8d31e5cda56e5eed
- dist/styles.css: 441a7bee13934ac40e86b3d016df5f6859fee107
- dist/header.js: 6ea938bc792b4e297b224e5aa38e118f68b97b52
- scripts/check.py: 8457415922c0f448d4d9fa1f361398d81be71054

## Executado

- `python scripts/check.py`: PASS — 18 links, 12 IDs únicos, 2 imagens; destinos, assets HTML, metadados e noindex da prévia. Materialização local contém os arquivos necessários ao header; assets remotos fora do escopo são preservados pela árvore base.
- `node --check dist/header.js`: PASS.
- Casos temporários direcionados ao check: aceita JS local existente com defer; rejeita URL externa, URL relativa a protocolo, arquivo inexistente, ../fora, fuga codificada (%2e%2e) e ausência de defer. Nenhuma dependência nova.
- Servidor HTTP temporário somente no loopback, encerrado após verificar HTTP 200 e igualdade de bytes de index.html, styles.css, header.js, wordmark, InterVariable.woff2 e logo legado. Isso comprova entrega dos arquivos no terminal, não renderização.
- Logo atual 25:15 comparado à exportação local: bytes e pixels idênticos (PNG RGBA, 260 × 77, 7259 bytes). Fonte existente conferida pelo blob original; licença preservada.
- Revisão do diff: HTML anterior/posterior ao header idêntico, exceto inclusão de header.js com defer. Regras CSS fora do header preservadas; alias da fonte aplicado somente ao header. Footer mantém seu asset e sua marca.
- Revisão estática corrigiu padding horizontal desktop para 29 px, texto para preto e ordem de exibição/foco ao atravessar o breakpoint. Nenhuma interação foi apresentada como testada no browser.
- Parser CSS adicional não disponível (tinycss2 ausente); nada instalado. Isso não substitui nem bloqueia a validação no navegador da C.

## Comportamento implementado, ainda por conferir no navegador

- Grid organiza marca/navegação; lista linear usa Flexbox. Na referência de 16 px de raiz, logo 77 + padding vertical 46 + borda 2 totalizam 125 px. Altura pode crescer com o conteúdo.
- Largura da marca limitada à referência, proporção preservada; texto/ações não são escalados com transform.
- Abaixo de 95em, marca e Menu ficam na primeira linha, links abertos na segunda, no fluxo. Breakpoint é estimativa de encaixe, não resultado de teste visual.
- Sem JS: botão não aparece e os links permanecem visíveis. Com JS: aria-expanded, Escape, fechamento ao seguir âncora e transferência de foco em mudanças de largura.
- Projetos é texto pendente, sem âncora falsa; seu aviso visível diferencia a prévia do frame. Não corresponde a conteúdo final de produção.
- Hero e demais seções permanecem da V3; não avaliar suas diferenças como se fossem parte desta etapa.

## Checklist da C e evidências para revisão humana

Usar o commit final indicado no handoff, confirmar branch/HEAD e alterações locais, ler AGENTS.md e o contrato do header. Usar navegador/Python já existentes no Windows; não instalar nem publicar.

1. Executar o check e servir a pasta dist com o Python confirmado. Não assumir que py ou python existe antes de verificar.
2. Comparar a região do header em viewport 1920 × 1080 à captura atual 1920 × 125 após carregar a fonte; incluir logo, espaçamentos, texto, borda e Contato.
3. Conferir larguras 1440, 768, 390 e 320; janela baixa 1440 × 600 e paisagem 844 × 390. Redimensionar continuamente ao redor de 95em e com o menu aberto/fechado.
4. Exercitar Tab/Shift+Tab, Enter/Espaço, Escape, âncoras e foco nos dois sentidos do breakpoint. Conferir sem JS.
5. Conferir texto ampliado a 200%, zoom 200%/400% e texto longo temporário sem persistir alterações editoriais; não cortar controles/conteúdo/foco nem causar rolagem horizontal no header.
6. Conferir rede/fontes/imagens e console. Comparar áreas fora do header à base somente para regressões.
7. Entregar capturas desktop/mobile aberto/fechado identificadas por commit, viewport e zoom; listar resultados e diferenças com coordenadas/estado quando possível. Se houver erro, registrar a reprodução e devolver à coordenação antes de editar em paralelo.

O header só será encerrado depois da comparação renderizada, correções pertinentes e validação visual de Gabriel. Testes históricos abaixo não comprovam esta implementação.

---

# Histórico de verificação — versão 3

27/10/2026, Brasília. Revisão de mensagem orientada pelas referências; sem publicação.

## Executado na V3

- `check.py`, `prepare_release.py --origin https://gabisou.com --output build` e `check.py build --public`: aprovados. 17 links, 11 IDs, dois logotipos com alt e dimensões, recursos existentes, e-mail esperado, prévia sem indexação e release indexável. Geração de release não publica.
- Primeira tela e serviços inspecionados visualmente no desktop; primeira tela e serviços inspecionados em iframe de 320 px.
- Reflow nos iframes de 320, 390, 768 e 1024 px: áreas úteis de 305, 375, 753 e 1009 px; `scrollWidth` igual a `clientWidth` em todas. Nenhuma rolagem horizontal indevida. Não são dispositivos físicos.
- Ordem dos títulos confirmada nos quatro frames: serviços → sobre → processo → contato. Menu e rodapé acompanham a ordem.
- Teclado: primeiro Tab alcança “Pular para o conteúdo”, depois logo e Serviços; foco sólido visível. Enter em Serviços levou a `#solucoes`. Âncora Serviços também acionada no frame de menor largura.
- Destinos dos links e endereço mailto preservados e verificados estaticamente; nenhum e-mail enviado. Recebimento continua não testado.
- CSS e ativos não alterados nesta revisão. Os cálculos de contraste da V2 abaixo continuam aplicáveis; não houve nova auditoria completa de contraste.
- Release: seis arquivos, 81.503 bytes sem compressão; 57.264 bytes em estimativa gzip. Não é medição de rede, Lighthouse ou dados reais de uso.
- HTML de prévia portátil gerado com CSS, favicon e logotipo incorporados. A página interna de QA não integra código sincronizado, release ou entrega.
- Textos próprios e vinculados aos serviços confirmados. Sem cases, equipe permanente, números, clientes ou parcerias inventados. Evidências, limitações e próxima tarefa registradas em `CONTINUIDADE.md` e `REFERENCIAS-E-MENSAGEM.md`.

## Limites atuais

Sem teste de recebimento, auditoria integral WCAG 2.2, leitor de tela, aparelhos físicos, vários navegadores, Lighthouse ou métricas de campo. WhatsApp não foi incluído sem número confirmado. Hospedagem e aprovação editorial seguem pendentes. A comparação de concorrentes cobre conteúdo e navegação, não qualidade visual ou técnica completa.

---

## Histórico de verificação — versão 2

27/10/2026, Brasília. Versão baseada no material da designer. Implementação revisada, sem publicação.

## Executado

- Scripts `check.py`, `prepare_release.py` e `check.py build --public`: aprovados; 17 links, 11 IDs únicos, dois logotipos com alt e dimensões, recursos existentes, e-mail correto, indexação de prévia/produção coerente.
- Página principal e rodapé inspecionados visualmente no desktop. Primeira tela inspecionada em larguras de celular.
- Reflow após mudanças finais em iframes de 320, 390, 768 e 1024 px: áreas úteis 305, 375, 753 e 1009 px; scrollWidth igual a clientWidth. Sem rolagem horizontal. Não são dispositivos físicos.
- Cabeçalho móvel ajustado para que ordem visual e DOM coincidam. Tab após o logo levou a Sobre; Sobre, Serviços e Contato têm mesma linha e ordenação. Alvos dessa navegação medem 35×44, 50×44 e 108×51 px na largura mínima.
- Links do rodapé conferidos com seus destinos; altura mínima 44 px, exceto o logo com 43 px e 138 px de largura. Âncoras existentes, sem botões inertes.
- Navegação do contato e rodapé observada no navegador. Email é link mailto; não houve envio nem teste de recebimento. Instagram tem o destino já publicado no site original, mas o perfil não foi reautenticado ou auditado.
- Revisão estática independente de contraste e conteúdo. Contrastes calculados: texto do cabeçalho 4,68:1; branco nos botões/rodapé 6,03:1; texto secundário do rodapé 5,07:1; foco branco sobre azul 3,65:1; foco laranja nos fundos claros ≥3,87:1. Textos do exemplo ilustrativo também acima de 4,5:1.
- HTML em português, um H1, títulos e landmarks preservados. Imagens com descrição; ícones decorativos ocultos da árvore acessível. Preferência por movimento reduzido respeitada.
- Produção com seis arquivos, 81.332 bytes sem compressão. Estimativa gzip 57.183 bytes. Não são medições de transferência ou pontuações Lighthouse.
- Código de produção sem JavaScript de execução, fontes externas, formulário, rastreadores ou dependências. Live reload pertence apenas ao servidor de prévia.
- Oferta de design explicitada sem inventar vínculo empregatício, equipe, case, certificação, cliente ou condição comercial. Projetos de preenchimento não publicados.

## Limites

Sem auditoria completa WCAG 2.2, leitor de tela, teste em aparelho físico, bateria entre navegadores, Lighthouse ou métricas de usuários reais. Nenhuma pontuação ou conformidade integral declarada. O recebimento de e-mail não foi testado. Número de WhatsApp ausente. Hospedagem, configuração de DNS e processo de rollback ainda precisam ser confirmados. Texto e processo aguardam aprovação editorial.

## Referências

- https://www.w3.org/WAI/WCAG22/quickref/
- https://www.w3.org/WAI/WCAG22/Understanding/contrast-minimum.html
- https://developers.google.com/search/docs/fundamentals/get-started-developers
- https://developers.google.com/search/docs/fundamentals/seo-starter-guide
- https://web.dev/articles/vitals
- https://gabisou.com/ — identidade e contatos inspecionados em 27/10/2026.
- Cinco wireframes anexados por Gabriel — direção visual da designer, não prova de projetos executados.
