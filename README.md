# GABiSOU — versão comercial do site (V3)

Página em português para apresentar design de interfaces, sites, sistemas, aplicativos, integrações, automações e aplicações de IA. A versão 3 preserva a direção visual dos cinco wireframes fornecidos pela designer e refina a mensagem após analisar seis referências indicadas por Gabriel. O header e a seção Projetos do redesign usam HTML/CSS nativo, com JavaScript local para o Menu; as demais seções continuam na V3. Projetos contém somente os três placeholders autorizados do Figma; “Ver mais” permanece desabilitado até definir seu destino. Sem dependências de produção, formulário ou rastreadores. Logotipo original recuperado de `https://gabisou.com/logo.png` em 27/10/2026.

## Estado

Versão implementada para revisão. Nada publicado; domínio, site atual e branch principal preservados. `dist/` contém a prévia sem indexação. O e-mail veio do site atual; a caixa não foi acessada e o recebimento não foi testado. WhatsApp omitido até confirmação do número.

## Revisar localmente

No Windows de Gabriel, o padrão é `C:\Repos`; este clone fica em `C:\Repos\gabisou.github.io`. Setup comprovado em 28/10/2026: Python 3.13.15, check aprovado e renderização no navegador integrado do aplicativo. Branch `codex/figma-redesign`; base atual `eaa38db79d388901e273abb4d54ad6fa8703158d`, incorporada por fast-forward em 29/10/2026. Header/Projetos estão modificados localmente, sem commit/push, aguardando revisão técnica e validação visual humana. Checks: PASS (19 links, 14 IDs, 2 imagens). Detalhes, diferenças e capturas em [VERIFICACAO.md](docs/VERIFICACAO.md); o registro do setup de 28/10 foi preservado.

Na raiz do clone, em PowerShell:

```powershell
Set-Location 'C:\Repos\gabisou.github.io'
python -X utf8 scripts/check.py
python -m http.server 8000 --bind 127.0.0.1 --directory dist
```

Abra `http://localhost:8000/` (mesmo servidor local em 127.0.0.1); mantenha o terminal ativo e use `Ctrl+C` para parar. Se a porta estiver ocupada, escolha outra sem encerrar processos desconhecidos. Nenhuma instalação de pacote é necessária. `dist/` contém fontes editáveis versionadas. A comprovação técnica não constitui aceite visual. A aba antiga em 127.0.0.1 reteve JavaScript anterior durante o QA; as evidências finais usam a origem local `localhost` recém-aberta.

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
- Referências e direção de mensagem: `docs/REFERENCIAS-E-MENSAGEM.md`.
- Textos e orientação para design: `docs/CONTEUDO-PARA-DESIGN.md`.
- Contexto, fontes e próxima tarefa: `docs/CONTINUIDADE.md`.
- Resultados e limites dos testes: `docs/VERIFICACAO.md`.

Após mudar a fonte, gere novamente `build/` e repita a verificação. Não edite só os arquivos gerados.
