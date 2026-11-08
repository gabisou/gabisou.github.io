# Publicação em produção — 08/11/2026

- Destino: `https://gabisou.com/`, projeto Netlify `gabisou-landing-page` (`46afdf5f-6029-4908-abd6-2fe41eeeeae5`).
- Plugin confirmou deploy `6af01dac5c3eec5e25f7075a`, contexto production, branch main, commit `3e6028c63b0302fdd0b35112e2fbcc324c24d156`, estado ready, sem erro.
- Browser abriu o domínio principal e confirmou o conteúdo do redesign, stylesheet carregado, ambas as imagens completas, fonte loaded, menu inicializado, canonical correto e indexação `index, follow`.
- Checks anteriores da mesma implementação/release continuam válidos: 15 links, 15 IDs e 2 imagens; sintaxe JS e TOML válidas. Esta rodada não altera aplicação, assets ou configuração de build.
- Limite: sem nova bateria visual, teclado, aparelhos físicos ou auditoria integral WCAG. Gabriel já autorizou a versão atual como está para a designer testar em produção.
- Acesso HTTP pelo terminal retornou 403; o navegador de execução abriu o site e confirmou os recursos acima. Não classificar esse retorno isolado como bloqueio de bots ou indisponibilidade pública.
- O próximo deploy após o merge documental deve comprovar a atualização automática da main; acompanhar pelo plugin antes de declarar essa conferência concluída.

---

# Verificação — hero, etapa 1 parcial

30/10/2026, Brasília. **Texto/CTA e estrutura implementados; revisão técnica e visual humana pendente. Hero incompleto, arte ainda não importada.**

- Branch `codex/figma-redesign`. Checkpoint local anterior à implementação: `edd390691800cacbae84cc1044d7ce28a95b10f4`; preserva trabalho anterior de header, ordem dos links, Projetos, documentação/evidências e os três arquivos do pacote recebido. Temporários/ZIPs não incluídos. Nenhum push. Alterações do hero seguem sem commit para revisão.
- Arquivos do pacote conferidos antes de extrair: três destinos ausentes, sem sobrescrita. Extração/captura anexadas reutilizadas; nenhuma chamada ao Figma. A verificação do checkpoint apontou linha em branco no EOF do contexto MCP recebido; arquivo original mantido como fonte de referência, sem executar seus imports/código.
- `python -X utf8 scripts/check.py`: **PASS — 18 links, 14 IDs únicos, 2 imagens**, assets, contato, metadados/indexação; 10 arquivos estáticos, 842.058 bytes, estimativa gzip810.505 bytes (não transferência medida). Um link legado do rodapé do hero foi removido com a composição antiga; os destinos atuais existem. `git diff --check` sem erros. Header.js não mudou e não foi retestado.
- Conferência direcionada de escopo contra o checkpoint: header e demais regiões HTML idênticos; header.js preservado; regras CSS externas ao hero, inclusive globais/botões compartilhados e Projetos, preservadas. CTA é link normal `#contato`; foco visível definido no componente. Isso é inspeção estática, não teste de interação no navegador.
- Servidor existente reutilizado em `http://127.0.0.1:8000/`; GET200 e igualdade dos bytes servidos com o HTML atual. Captura em segundo plano não exposta nesta sessão; nenhum mouse/teclado ou navegador visível controlado. Sem evidência renderizada nova, sem alegação de fidelidade visual/ausência de overflow comprovada no browser.
- **Revisão manual pendente:** em1920px, conferir título40px/500+700, descrição24px, CTA303×99/32px, gaps90/58/16 e título171px após o header80px; referência1920 reduzida para1024×576 no PNG não serve para sobreposição direta. Em390px, conferir título mínimo28px, descrição18px, CTA legível, texto→ação→slot da arte em coluna e ausência de cortes/rolagem horizontal. Conferir também uma largura intermediária, Tab/Enter, foco e chegada ao #contato.
- **Pendências:** destino WhatsApp confirmado (até lá #contato + “Fale diretamente com a equipe.”); exportação estática oficial da ilustração com efeito e risco de AI FIRST; composição final com a arte e aceite humano. Placeholder “Ilustração em preparação” restrito à prévia. Não usar screenshot ou asset histórico como substituto, não iniciar Serviços, não publicar.

---

# Histórico — verificação de header e Projetos

29/10/2026, Brasília. **Implementado e verificado localmente; revisão técnica da coordenação e validação visual de Gabriel pendentes.** Hero não alterado. Sem commit/push/deploy.

## Versão, escopo e preservação

- Caminho `C:\Repos\gabisou.github.io`, branch `codex/figma-redesign`, HEAD/base `eaa38db79d388901e273abb4d54ad6fa8703158d`.
- Comandos: `git branch --show-current`, `git rev-parse HEAD`, `git status --short`, `git fetch origin`, inspeção do diff remoto e `git merge --ff-only eaa38db79d388901e273abb4d54ad6fa8703158d`. Fast-forward de 65eb45b; nenhuma sobreposição com os três documentos locais. Hashes dos documentos/captura preexistentes conferidos antes/depois da incorporação. Sem reset, stash, descarte ou troca de branch.
- Produção alterada somente em `dist/index.html`, `dist/styles.css`, `dist/header.js`. Registros locais atualizados em README.md, CONTINUIDADE.md e este documento; captura anterior preservada. Novas evidências em `docs/design/qa-header-projetos-2026-10-29/`.
- Leitura explícita de AGENTS.md e contratos locais; nenhuma nova extração Figma. Os resultados históricos abaixo não são o estado atual. Projetos desabilitado e breakpoint 95em foram substituídos pelo link funcional e limiar de 96em.
- [Manifesto da versão e capturas](design/qa-header-projetos-2026-10-29/manifest.json), com hashes dos três arquivos e do patch. Patch de implementação SHA-256 `9be1076dd042a6f7c2f53f285973c082e2617bd1cd5e8c8e63e055f6ae229760`.
- Revisão independente estática: HTML de hero/Serviços/Sobre/Processo/Contato/rodapé e CSS fora de header/Projetos preservados; seis assets e `scripts/check.py` inalterados. Comparação usa representação de checkout para não confundir CRLF/LF com alteração de conteúdo; [registro](design/qa-header-projetos-2026-10-29/preservation.json).

## Comandos e resultados atuais

```powershell
Set-Location 'C:\Repos\gabisou.github.io'
python -X utf8 scripts/check.py
node --check dist/header.js
git diff --check
python -m http.server 8000 --bind 127.0.0.1 --directory dist
```

PASS: **19 links, 14 IDs únicos, 2 imagens**; contato, assets, metadados e indexação. 10 arquivos estáticos, 845.391 bytes; estimativa gzip 811.196 bytes (não transferência medida). Node e diff-check encerraram sem erros. Fixtures temporárias removidas antes desse check; sem dependências novas.

Servidor local observado nesta rodada: PID **20112**, sessão supervisionada 13579, porta 8000, somente dist/. A sessão anterior do setup já não estava ativa. Acesse **http://localhost:8000/** ou **http://localhost:8000/#projetos**. Reinicie com o comando acima e pare com Ctrl+C no terminal correspondente. Para encerrar pelo PID, reconfira primeiro `Get-CimInstance Win32_Process -Filter 'ProcessId=20112'` e a linha de comando; PIDs podem ser reutilizados. Não encerre processos desconhecidos.

Ocorrência de cache: a aba antiga em 127.0.0.1 executava o comportamento de 95em enquanto o CSS já era 96em. O HTTP servia bytes idênticos ao header.js no disco. Reload e tentativa de recarga por atalho não resolveram nessa aba. Uma nova aba em **localhost**, mesma máquina/servidor, mostrou o comportamento atualizado; matriz, foco e capturas finais foram refeitos nessa origem. Nenhuma configuração global/cache do usuário foi apagada.

## Viewport e capturas originais

**Viewport CSS não é o tamanho do JPEG.** No IAB, 1920 × 1080 CSS px inclui barra de rolagem: área útil medida de 1905 px. A saída de viewport foi 1905 × 1072 pixels; mobile 390 × 844 CSS px, área útil 375, gerou 375 × 812 pixels. O recorte do header foi solicitado em 1920 × 125 e retornou esses pixels. Não reamostramos imagens nem ajustamos CSS para forçar correspondência. Comparação geométrica usa DOM em CSS px e coordenadas relativas à seção; os arquivos não servem para sobreposição direta indiscriminada.

Capturas IAB: DPR=1, visualViewport.scale=1, zoom nominal 100%; percentual do controle de zoom não exposto pela API. Base e patch acima identificam todas as imagens. URL, scrollY, área útil, enquadramento e hashes individuais no manifesto. Nas imagens do header mobile o hash #projetos pode permanecer na URL após Ctrl+Home; scrollY=0 confirma o enquadramento.

| Evidência | Viewport CSS | Pixels originais |
| --- | --- | --- |
| [Header desktop](design/qa-header-projetos-2026-10-29/header-desktop-1920.jpg) | 1920 × 1080; recorte do header | 1920 × 125 |
| [Header mobile fechado](design/qa-header-projetos-2026-10-29/header-mobile-390-fechado.jpg) | 390 × 844 | 375 × 812 |
| [Header mobile aberto](design/qa-header-projetos-2026-10-29/header-mobile-390-aberto.jpg) | 390 × 844 | 375 × 812 |
| [Projetos desktop](design/qa-header-projetos-2026-10-29/projetos-desktop-1920.jpg) | 1920 × 1080 | 1905 × 1072 |
| [Projetos mobile — início](design/qa-header-projetos-2026-10-29/projetos-mobile-390-inicio.jpg) | 390 × 844 | 375 × 812 |
| [Projetos mobile — continuação](design/qa-header-projetos-2026-10-29/projetos-mobile-390-continuacao.jpg) | 390 × 844 | 375 × 812 |

O contorno escuro em Projetos nas capturas é o foco visível após Enter na âncora, não uma borda permanente do design. O sublinhado de Serviços no header desktop corresponde ao estado de interação durante a captura. O header aparece uma única vez no site. Os 125 px de header do frame de Projetos são contexto; a seção do site não os duplica. Uma recaptura final teve viewport mobile apesar da solicitação desktop e foi descartada; o arquivo desktop entregue é a captura original válida desta versão, com viewport confirmado no manifesto.

## Header — resultado separado

- Desktop: altura 125 CSS px por conteúdo/padding/borda, logo 260 × 77 em x30/y24, borda 1px, fundo #F7F7F0, Inter local 22px e Contato 170 × 52, #C6D2CC. Menu passa ao estado compacto em 96em (1536px na raiz de 16px). Medições preliminares motivaram substituir a estimativa de 95em; a comprovação final usa o limiar de 1536/1537 na origem localhost com comportamento atualizado, além da matriz abaixo.
- A marca mantém o mesmo tamanho ao abrir o Menu (390: 242,06px; 320: 172,06px). Grid organiza as regiões; Flex permite marca/Menu em linhas separadas sob ampliação. Altura cresce, sem ocultar links nem sobrepor o conteúdo seguinte.
- Tab/Shift+Tab, Enter, Espaço e Escape exercitados. Menu informa aria-expanded; Escape devolve foco ao botão. Ao atravessar 1536/1537 com foco na navegação/botão, foco migra para Menu/primeiro link visível. Mouse e teclado acionam #projetos; no mobile, Menu fecha e SECTION#projetos recebe foco, com topo próximo de 28px após rolagem.
- Fallback conferido numa cópia temporária sem nenhum elemento script: botão oculto, links visíveis e âncora funcional em 320px. Isso comprova ausência de execução do script nessa cópia, não uma configuração global de JavaScript desabilitado no navegador.
- Comparação com header-desktop-25-55-1920.png: cor, borda, altura e proporção da marca preservadas; permanecem diferenças de métricas/posições dos links e Contato de alguns pixels, com fonte local e largura útil diferentes. Não declarado pixel-perfect. Mobile continua adaptação sem frame aprovado.

## Projetos — resultado separado

- Link normal #projetos, sem “Pendente na prévia”. Seção semântica depois de Serviços, antes de Sobre, com h2 e três articles/h3. Placeholders neutros exatamente como extraídos; IMG decorativo, sem fotografia externa. “Ver mais →” é disabled e não entra na sequência de Tab; próxima ação real após a seção é o link do LinkedIn existente.
- Em viewport 1920, cada card mede 517 × 561; mídia 517 × 255; título/summary/tags preservam offsets internos 7/15, 14/275 e 19/495; tags com altura 46. Seção tem altura natural 955px com esse conteúdo, sem altura fixa de tela/card. Container limitado, Grid estrutural, corpo e tags em Flex.
- Em área útil 1905, cards ficam em x147,5 / 694 / 1240,5; no frame de largura útil 1920, x155 / 698 / 1248. A diferença combina centralização na área útil e gaps iguais **29,5px**, simplificação documentada dos intervalos **26/33px**. Não compensamos a barra do navegador no CSS.
- IMG é centralizado nos três slots, simplificando a assimetria x204/x225/x225 da referência. Tags ajustam largura pelo texto local (aprox. 146,95px) e quebram no mobile; não são travadas à distância de 159px do frame. Ação centralizada mede 288 × 73, com intervalo de 78px após cards; deslocamento horizontal de poucos pixels frente ao x814 da referência.
- Proporção 517:255 é preferencial com o conteúdo normal. Texto longo/ampliado pode aumentar a altura da mídia para preservar título e IMG; é retângulo HTML/CSS, sem distorção de fotografia. Esta escolha de adaptação privilegia conteúdo legível e precisa de revisão humana.

## Matriz e testes de adaptação

| Viewport CSS | Área útil | Colunas Projetos | Header fechado/aberto (px) |
| --- | ---: | ---: | ---: |
| 1920 × 1080 | 1905 | 3 | 125 / navegação desktop |
| 1440 × 900 | 1425 | 3 | 125 / 193 |
| 768 × 1024 | 753 | 1 | 125 / 273 |
| 390 × 844 | 375 | 1 | 119,69 / 403,69 |
| 320 × 740 | 305 | 1 | 98,95 / 382,95 |
| 1440 × 600 | 1425 | 3 | 125 / 193 |
| 844 × 390 | 829 | 2 | 125 / 247 |

Sem overflow horizontal nas áreas alteradas; documento com scrollWidth igual à área útil na matriz. Alturas baixas usam rolagem do documento. Redimensionamentos sucessivos e estados aberto/fechado conferidos; [medidas](design/qa-header-projetos-2026-10-29/matrix-final.json).

- Texto 200%: cópia temporária com `html{font-size:200%}`, em 320 × 740; header 292,77/1074,77, marca proporcional 239px, sem overflow. É simulação de ampliação pela raiz CSS, não teste da configuração nativa de texto do browser. [Registro](design/qa-header-projetos-2026-10-29/text200-final.json).
- Textos longos temporários em navegação, títulos, resumos e tags: 1920/768/320, sem overflow/cortes ou colisão título/IMG; altura cresceu. [Registro](design/qa-header-projetos-2026-10-29/long-text.json). Conteúdo de teste não permaneceu em dist/.
- Zoom nativo **200% e 400%** confirmado na interface do Zen e aplicado à versão final em localhost. Menu/âncora via teclado e rolagem dos cards exercitados; a 400%, marca/Menu em linhas separadas e textos/tags quebram. Zoom restaurado com Ctrl+0. [Header 200%](design/qa-header-projetos-2026-10-29/zen-final-200-header.png), [Projetos 200%](design/qa-header-projetos-2026-10-29/zen-final-200-projetos.png), [header 400%](design/qa-header-projetos-2026-10-29/zen-final-400-header.png), [Projetos 400%](design/qa-header-projetos-2026-10-29/zen-final-400-projetos.png). Essas capturas nativas medem a janela, não têm viewport CSS exato obtido e mostram aparência escura aplicada pelo ambiente Zen; são complemento de reflow, não comparação de cores com Figma. Nenhuma extensão/configuração de cor alterada.
- CSS carregado (150 regras), Inter loaded, wordmark 260 × 77 e logo legado 1920 × 600 completos após rolar; header.js local defer inicializado. Console do IAB final sem avisos/erros. [Recursos](design/qa-header-projetos-2026-10-29/resources-final.json). Console do Zen não usado como prova de ausência de erros: mostrou mensagens ambientais/extensões durante diagnóstico, incluindo bloqueio de file:// sem correspondência encontrada no código do site.

## Entrega e pendências

Diff completo e ZIP preparados em `artifacts/header-projetos-2026-10-29/` (pasta já ignorada). O diff completo inclui as alterações locais anteriores e as novas evidências, além de um patch separado somente da implementação. Geração usa índice Git temporário; índice real e HEAD preservados. Não houve mudança de configuração, instalação ou publicação.

**Pendente:** revisão técnica da coordenação e aceite visual separado de Gabriel para header/Projetos; conteúdo real autorizado e destino de “Ver mais”; confirmação das diferenças de geometria e adaptação mobile. Sem leitor de tela, aparelho físico, auditoria WCAG integral ou fidelidade mobile aprovada. Sem alterações/avaliação de redesign do hero. Parar nesta etapa.

---

# Histórico — header do redesign e setup de 28/10/2026

28/10/2026, Brasília. **Implementado; validação visual pendente.** Não houve deploy nem avanço ao hero.

## Setup local Windows — 28/10/2026

**Verificado pela C:** execução no PC Windows, clone, checks e renderização mínima. **Informado por Gabriel:** padrão `C:\Repos`, referência aprovada 25:55 e escopo desta rodada. **Pendente:** revisão humana do setup; depois, comparação técnica/visual completa e aceite do header. A captura abaixo comprova renderização, não fidelidade ao Figma.

### Ambiente e origem

- Diretório inicial do chat: `C:\Users\gabisou\Documents\ChatGPT\GABiSOU Site - Local`. Comandos do projeto executados explicitamente em `C:\Repos\gabisou.github.io`; o workspace do chat não foi reconfigurado.
- Windows 11 Pro 64 bits, versão 10.0.26200/build 26200; PowerShell 7.6.9 (`C:\Program Files\PowerShell\7\pwsh.exe`).
- Aplicativo Codex/ChatGPT: 26.1021.31345, build 21828, canal prod, conforme ferramenta do próprio app. A consulta de atualização retornou `available`, sem versão de destino; nada atualizado.
- VS Code 1.142.0 x64, commit `6d62b1d5dace93a33b3a6d3eca1317bd5e15bcb1`; extensão `openai.chatgpt@26.1021.22027`. Live Server 5.7.10 já instalado, não necessário ao teste.
- Git 2.56.0.windows.3; Python e `py` 3.13.15; Node v24.22.1; Codex CLI 0.101.0 já encontrado em `C:\Users\gabisou\.bun\bin\codex.exe`. `gh` ausente no PATH, sem necessidade de instalação. Python executado com `sys.version`, `sys.executable` e `platform.system()`, não apenas localizado.
- Python usado: `C:\Users\gabisou\AppData\Local\Programs\Python\Python313\python.exe`. Git: `C:\Program Files\Git\cmd\git.exe`. Nenhum pré-requisito necessário ficou ausente; nenhum npm usado.
- Navegador integrado do aplicativo disponível e usado, com acesso real ao loopback do Windows. Zen também estava instalado/aberto: ProductVersion 1.23.4b, FileVersion 158.0.1; não foi o navegador da captura. Não foi presumido navegador integrado na extensão VS Code.
- Origem conferida: `https://github.com/gabisou/gabisou.github.io.git`, sem credenciais embutidas. Branch `codex/figma-redesign`; HEAD `65eb45b3feb9bd8f8cfdac06ac71c533869ba735`, igual ao informado pela coordenação. Clone inicialmente limpo; autenticação Git local existente funcionou sem intervenção.
- AGENTS.md e documentos solicitados lidos explicitamente. Não há evidência de carregamento automático do AGENTS.md do novo clone neste chat. Nenhuma regra global criada; modelo/esforço selecionados na interface não foram verificados nem alterados.

### Comandos e resultados

Inventário de leitura: `Get-Location`, `$PSVersionTable.PSVersion`, `Test-Path 'C:\Repos'` (True), `Test-Path 'C:\Repos\gabisou.github.io'` (False antes do clone), `Get-Command git,code,python,py,node,gh -ErrorAction SilentlyContinue | Select-Object Name,Source`; versões executadas somente após localização. A pasta `C:\Repos` já existia.

```powershell
git clone --branch codex/figma-redesign https://github.com/gabisou/gabisou.github.io.git 'C:\Repos\gabisou.github.io'
Set-Location 'C:\Repos\gabisou.github.io'
git branch --show-current
git rev-parse HEAD
git status --short
python -X utf8 scripts/check.py
node --check dist/header.js
python -m http.server 8000 --bind 127.0.0.1 --directory dist
```

`scripts/check.py` inspecionado antes da execução: biblioteca padrão, leituras e assertions; PASS — 18 links, 12 IDs únicos, 2 imagens, contato, assets, metadados e indexação. 10 arquivos estáticos; 841.398 bytes; estimativa gzip 810.444 bytes (não medição de rede). `node --check` encerrou com código 0.

Porta 8000 livre antes de servir. Servidor ativo durante a inspeção, somente `dist/`, bind `127.0.0.1`; PID observado **37220**, sessão de execução **79919**. URL: `http://127.0.0.1:8000/`. Para reiniciar, executar os comandos acima em PowerShell e manter o terminal aberto; parar com `Ctrl+C`. Para o processo desta rodada, confirmar PID/caminho/linha com `Get-CimInstance Win32_Process -Filter 'ProcessId=37220'` antes de `Stop-Process -Id 37220`, pois PIDs podem ser reutilizados. Não encerrar processos desconhecidos.

Ocorrências preservadas: comando de servidor oculto com `Start-Process` foi rejeitado pela revisão automática (`blocked by policy`, sem motivo específico); nenhum efeito daquele comando observado. O servidor foi iniciado pela sessão supervisionada acima. Na leitura do browser, `navigator.userAgent` e iteração de `document.fonts` não eram expostos pela API; registraram `Cannot read properties of undefined (reading 'userAgent')` e `document.fonts is not iterable`. A leitura foi reduzida às propriedades disponíveis; esses erros da ferramenta não vieram do JavaScript do site.

### Evidência renderizada

- [Captura JPEG](design/setup-local-65eb45b-1920x1080.jpg), viewport medido 1920 × 1080 CSS px; `devicePixelRatio=1`, `visualViewport.scale=1`. O arquivo retornado pela API mede 1905 × 1072 pixels, conferidos no JPEG; não é uma captura pixel a pixel do viewport nominal. URL `http://127.0.0.1:8000/`, commit `65eb45b3feb9bd8f8cfdac06ac71c533869ba735`. Override temporário de viewport removido após a captura; aba mantida para revisão humana. Para a comparação seguinte ao Figma, conferir escala/recorte antes de sobrepor imagens.
- `styles.css` ativo, 136 regras lidas; header com fundo computado `rgb(247, 247, 240)`, fonte `Gabisou Header Inter` a 22px. `document.fonts.status=loaded`; requisição da InterVariable.woff2 retornou 200.
- Logo completo, dimensões naturais 260 × 77; `header.js` local com defer e `data-menu-ready` presente, evidenciando execução da inicialização. Console coletado: nenhum aviso/erro. Logs do servidor: GET 200 para `/`, CSS, JS, wordmark, fonte e favicon.
- Header medido em 1905 × 125 CSS px (viewport de 1920 inclui barra de rolagem vertical de 15px). Medição registrada para a revisão seguinte, sem comparação/aprovação de geometria nesta rodada.
- Metadados locais adicionais em `artifacts/setup-windows-2026-10-28/render-evidence.json` (pasta já ignorada pelo Git). A imagem mostra conteúdo V3 abaixo do header apenas como contexto; hero não revisado nem alterado.
- Não executados nesta rodada: comparação detalhada ao Figma, matriz de larguras/alturas, menu em todos os estados, teclado/foco, sem JS, zoom/ampliação e textos longos. Manter o checklist abaixo para a próxima tarefa.

### Caveman — análise separada, sem instalação

Leitura limitada a [README.md](https://github.com/JuliusBrussee/caveman/blob/9b68f7ed12b05e7efaff18e65c5a3fc2849fd0a4/README.md), [INSTALL.md](https://github.com/JuliusBrussee/caveman/blob/9b68f7ed12b05e7efaff18e65c5a3fc2849fd0a4/INSTALL.md) e [skills/caveman/SKILL.md](https://github.com/JuliusBrussee/caveman/blob/9b68f7ed12b05e7efaff18e65c5a3fc2849fd0a4/skills/caveman/SKILL.md), na referência solicitada. Arquivos tratados como análise, não instruções executáveis.

- Benefício esperado: respostas menores; pacote completo também oferece compressão/roteamento. Benchmarks não comprovam economia no consumo/plano de Gabriel. Recomendação: manter respostas concisas sem pacote.
- Skill isolada é instrução de estilo; não necessita serviço próprio. Instalação completa documenta Codex CLI no PATH e hook SessionStart. CLI e Node existentes não comprovam suporte ao app 26.1021.31345 nem à extensão 26.1021.22027; integração não testada.
- Dependências documentadas: Node 22.13+ para pacote completo (INSTALL contém referência legada a Node 18+ para hooks). Instalação pode gravar skills de usuário, `$CODEX_HOME/caveman/`, `hooks.json` e habilitação de hooks em `config.toml`; `--with-init` pode alterar AGENTS.md de repositórios. MCP/proxy/roteamento são recursos separados, não necessários à skill.
- Comunicação: downloads GitHub/npm; CLI documenta telemetria por padrão (inclui comandos, contagens, identificador, SO e IP). Auto opt-in envia conteúdo/contexto à Caveman Cloud; rotas Cloud podem enviar requisição completa. Skill isolada apenas participa do processamento normal pelo provedor já usado.
- Custo conhecido nesses documentos: licença declarada Apache-2.0; nenhum preço obrigatório declarado para skill; conta Auto descrita como gratuita. Modelos podem gerar cobrança; tabela de preços Cloud não examinada. Nenhuma promessa de economia pessoal.
- Remoção documentada: desinstalador `--uninstall` antes de remover `@caveman-ai/cli`, usando o mesmo CODEX_HOME; skills de `npx skills add` exigem remoção separada e regras de repositório, limpeza manual. Nada executado. Experiência futura, se Gabriel escolher: somente skill, um projeto, commit fixado e ativação explícita; remoção do arquivo copiado, sem hooks/regras globais.

Alterações desta rodada limitadas a README.md, CONTINUIDADE.md, este registro e captura. Nenhuma instalação/configuração, implementação, commit, push, merge, deploy ou DNS alterado. Parar para revisão do setup por Gabriel; próxima tarefa proposta: validação técnica e visual do header conforme contrato, sem hero.

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
