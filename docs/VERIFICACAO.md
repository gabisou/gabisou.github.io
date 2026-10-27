# Verificação — versão 2

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
