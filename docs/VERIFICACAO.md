# Verificação da primeira versão

Data: 27/10/2026, Brasília. Estado: implementação revisada; publicação não realizada.

## Executado

- HTML em português, um H1, títulos, landmarks, navegação e textos alternativos revisados.
- 13 links verificados estruturalmente, 11 IDs únicos, destinos de âncoras existentes e dois logotipos carregados.
- E-mail `gabisoudev@gmail.com` conferido no site existente e nos três links `mailto:`. Assunto e mensagem inicial codificados corretamente. Não houve envio nem teste de recebimento.
- Navegação real até serviços e apresentação de Gabriel. Link de pular conteúdo acionado com teclado, seguido de Tab até o CTA. Foco visível inspecionado.
- Desktop revisado no navegador: viewport de 1363 px, área de documento de 1348 px.
- Reflow medido em iframes de 320, 390, 768 e 1024 px. Áreas úteis de 305, 375, 753 e 1009 px devido às barras verticais. Sem rolagem horizontal: scrollWidth igual a clientWidth. Não equivale a aparelhos físicos.
- Primeira tela e serviços inspecionados no desktop; primeira tela de celular e apresentação de Gabriel a 320 px também inspecionadas.
- Revisão independente identificou contraste insuficiente em texto do cartão azul: corrigido para `#414e75` sobre `#c5cff0`. Textos pequenos ampliados; exemplo recebeu `role="group"`.
- Foco laranja com contraste calculado de pelo menos 3,15:1 sobre fundos principais. Não constitui declaração de conformidade integral WCAG 2.2.
- `check.py`, `prepare_release.py` e `check.py build --public` executados com sucesso. Prévia sem indexação. Versão para o domínio existente com canonical, robots indexável, sitemap e dados reais de Organization.
- Produção: 80.597 bytes sem compressão; estimativa gzip 57.070 bytes. Não são transferência de rede medida nem pontuação Lighthouse.
- Sem dependências de produção, JavaScript de execução, fontes remotas, formulário, rastreadores ou coleta implementada pelo site. O servidor de prévia injeta live reload, ausente da produção.

## Limites e pendências

- Uma interrupção temporária do ambiente ocorreu durante a última revisão visual. Finalizar contato e percurso completo por teclado antes de publicar.
- Sem teste com leitor de tela, dispositivos físicos, Safari/Firefox ou auditoria completa de acessibilidade.
- Lighthouse e métricas de usuários reais não executados. Não há nota de desempenho.
- LinkedIn usa o destino publicado no site atual e localizado na pesquisa. Conteúdo profissional não foi importado como case ou endosso.
- WhatsApp omitido: falta número confirmado.
- Hospedagem, acesso de publicação, DNS, rollback e custos correntes não confirmados. Nenhum gasto, merge, publicação ou mudança de domínio realizado.
- Textos e processo são propostas editoriais pendentes de revisão pelo responsável. Sem preço, desconto, prazo comercial, case, cliente ou depoimento inventado.

## Referências consultadas

- https://www.w3.org/WAI/WCAG22/quickref/
- https://www.w3.org/WAI/WCAG22/Understanding/contrast-minimum.html
- https://developers.google.com/search/docs/fundamentals/get-started-developers
- https://developers.google.com/search/docs/fundamentals/seo-starter-guide
- https://web.dev/articles/vitals
- https://gabisou.com/ — identidade e contatos, inspecionados em 27/10/2026.
