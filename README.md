# GABiSOU — versão comercial do site

Página em português para apresentar sites, sistemas, aplicativos, integrações, automações e aplicações de IA. HTML/CSS sem JavaScript de execução, dependências de produção, formulário ou rastreadores. Logotipo original recuperado de `https://gabisou.com/logo.png` em 27/10/2026.

## Estado

Versão implementada para revisão. Nada publicado; domínio, site atual e branch principal preservados. `dist/` contém a prévia sem indexação. O e-mail veio do site atual; a caixa não foi acessada e o recebimento não foi testado. WhatsApp omitido até confirmação do número.

## Revisar localmente

Abra `dist/index.html` em um navegador. Opcionalmente, com Python instalado:

```sh
python -m http.server 8000 --directory dist
```

Depois abra `http://localhost:8000`. Nenhuma instalação de pacote é necessária.

## Verificar e preparar para publicação

```sh
python scripts/check.py
python scripts/prepare_release.py --origin https://gabisou.com --output build
python scripts/check.py build --public
```

Esses comandos apenas produzem e verificam arquivos. Não publicam, não alteram DNS e não configuram hospedagem. O domínio acima foi observado no site existente; sua manutenção como destino precisa ser confirmada antes do lançamento. `build/` recebe indexação, URL canônica, metadados da organização e sitemap. Publique apenas seu conteúdo, nunca a pasta de documentos ou a raiz do projeto.

Antes de implantar: aprovação editorial, confirmação da hospedagem atual e de como recuperar a versão anterior. Nenhum custo de serviço foi contratado. Não há pipeline de publicação automática neste projeto.

## Editar

- Conteúdo e destinos de contato: `dist/index.html`.
- Cores, espaçamento e responsividade: `dist/styles.css`.
- Identidade original: `dist/assets/logo.png`.
- Contexto, fontes e próxima tarefa: `docs/CONTINUIDADE.md`.
- Resultados e limites dos testes: `docs/VERIFICACAO.md`.

Após mudar a fonte, gere novamente `build/` e repita a verificação. Não edite só os arquivos gerados.
