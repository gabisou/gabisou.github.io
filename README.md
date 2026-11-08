# GABiSOU — site institucional

Site em HTML/CSS e JavaScript nativos. Fontes editáveis versionadas em `dist/`; scripts Python usam a biblioteca padrão. Sem framework, npm, backend ou dependências de produção.

## Estado e produção

Gabriel autorizou publicar a versão atual em `https://gabisou.com` para revisão contínua com a designer. O conteúdo ainda inclui placeholders autorizados; não apresentar esses elementos como portfólio final.

Repositório correto: `gabisou/gabisou.github.io`, da organização GABiSOU. Existe um repositório pessoal homônimo em `gabrieldevsouza`, que não é a fonte desta versão.

- `main`: integração e produção.
- Branches de tarefa: desenvolvimento e revisão; `codex/figma-redesign` contém o trabalho do redesign.
- Projeto Netlify existente: `gabisou-landing-page`, ID `46afdf5f-6029-4908-abd6-2fe41eeeeae5`.
- Vincular esse projeto ao repositório correto e à `main`. Cada merge/push nessa branch deve iniciar build e deploy automáticos. A confirmação do vínculo e do primeiro deploy permanece pendente no [checkpoint](docs/CONTINUIDADE.md).

## Desenvolvimento e revisão

Comece pela `main` atualizada e use uma branch de tarefa. Implemente o escopo aprovado, execute os checks, apresente a etapa para revisão e integre por pull request. O aceite visual de Gabriel continua necessário para mudanças visuais nas próximas etapas.

Na raiz do clone:

```sh
python -X utf8 scripts/check.py
node --check dist/header.js
python -m http.server 8000 --bind 127.0.0.1 --directory dist
```

Abra `http://localhost:8000/`. Não é necessário instalar pacotes. No laptop de Gabriel, os repositórios ficam em `C:\GitHub`; confirme o caminho do checkout em uso.

## Build de produção

O `netlify.toml` versionado executa os checks, limpa somente a saída gerada `build/`, prepara a origem `https://gabisou.com` e verifica a release pública. Publica exclusivamente `build/`, sem documentos ou fontes de suporte. Python 3.12 está declarado no ambiente de build.

Para preparar localmente, use uma saída nova ou limpa:

```sh
python -X utf8 scripts/check.py
node --check dist/header.js
python -X utf8 scripts/prepare_release.py --origin https://gabisou.com --output build
python -X utf8 scripts/check.py build --public
```

Gerar arquivos localmente não publica. `dist/` preserva os metadados de prévia; `build/` recebe indexação, canonical e sitemap de produção. Não edite somente a saída gerada. Para corrigir uma versão publicada, reverta o commit na `main` e deixe o mesmo fluxo publicar a correção.

## Arquivos principais

- Conteúdo e contatos: `dist/index.html`.
- Estilos e responsividade: `dist/styles.css`.
- Menu: `dist/header.js`.
- Assets e fontes: `dist/assets/`.
- Configuração de deploy: `netlify.toml`.
- Estado vigente e próxima ação: [CONTINUIDADE.md](docs/CONTINUIDADE.md).
- Critérios e evidências: [VERIFICACAO.md](docs/VERIFICACAO.md).
- Diretrizes técnicas: [ARQUITETURA-E-ETAPAS.md](docs/ARQUITETURA-E-ETAPAS.md).

Registros históricos não comprovam a versão atual nem substituem aprovações recentes.
