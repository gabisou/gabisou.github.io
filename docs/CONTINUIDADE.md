# GABiSOU — continuidade do site

## Estado atual — integração do redesign, 27/10/2026 (Brasília)

Esta seção substitui a próxima tarefa dos registros históricos abaixo. O redesign aprovado no Figma passa a ser a referência visual; a V3 não comprova sua reprodução.

- Base verificada: `codex/site-comercial-v1`, commit `857c326be11e4c335c4c508f8b4ee49995f590af`; PR #1 aberto em rascunho. `main` em `12a9196889ef93bf3597765daa360a286bb5e761` contém somente README e gitignore.
- Branch desta etapa: `codex/figma-redesign`, derivada dessa base. Alterações iniciais limitadas a AGENTS.md e este registro.
- Stack confirmada pela árvore e arquivos: HTML/CSS em dist; Python padrão para scripts; sem manifesto/lockfile, framework ou AGENTS.md anterior.
- GitHub: leitura de árvore, arquivos, branches, PR e resultados de CI funcionou. Conta conectada possui pull/push; ferramentas de escrita, branches e PRs estão expostas. Ausência de statuses, check-runs e workflow runs no commit base não equivale a CI aprovado.
- Figma: autenticação confirmada como gabisoudev, equipe no plano Starter, assento View. Ainda não houve leitura de frame: link/ID aprovado ausente. Cota restante desconhecida; evitar buscas e extrações redundantes.
- Ambiente A (nuvem): terminal e edição local funcionam; Python, Git e Node presentes. Recuperados dez arquivos pelo conector, com hashes Git conferidos, em cópia de trabalho sem .git. Isto não comprova acesso Git por terminal nem equivale ao PC de Gabriel.
- Verificação atual dessa base: `python scripts/check.py` aprovado (17 links, 11 IDs, 2 imagens); servidor Python respondeu HTTP 200 para página, CSS, logo e favicon. Playwright presente, mas lançamento falhou por falta do executável Chromium. Nenhuma comparação visual atual realizada.
- B: implementação preferencial no navegador, usando a base acima; confirmar plugins, escrita, terminal e navegador na sessão efetivamente escolhida. As capacidades de A não são automaticamente as de B.
- C: Windows, VS Code e Codex app/extensão informados por Gabriel, ainda sem inspeção local. Usar para conferência visual se B não tiver navegador funcional; não exigir CLI, Docker, WSL ou inferência local.
- Domínio registrado anteriormente: https://gabisou.com/. Hospedagem/DNS e fluxo de publicação não confirmados. Repositório informa GitHub Pages desativado. Nenhuma publicação autorizada nesta etapa.

### Referências do design

- Desktop aprovado (arquivo/frame/node-id): PENDENTE de Gabriel.
- Mobile aprovado: PENDENTE; existência ainda não confirmada.
- Tipografia, cores, espaçamentos, componentes, estados e assets do redesign: PENDENTES da primeira leitura.
- Não reutilizar cores, fontes ou ilustrações da V3 como se fossem decisões do redesign.
- Primeiro teste: criar sessão do arquivo e obter contexto + captura somente do cabeçalho/abertura aprovado, adaptando a HTML/CSS. Se houver quota/acesso bloqueado, registrar o erro e solicitar apenas captura nas dimensões do frame, especificações e assets dessa área.

### Próxima tarefa

Obter o link com node-id; realizar uma leitura real pequena; definir navegador de validação de B ou C; então implementar apenas cabeçalho/abertura desktop e mobile. Enquanto isso, C pode inspecionar seu ambiente sem editar o site. No cliente Codex, informar instruções carregadas antes de ler explicitamente AGENTS.md para distinguir carregamento automático de leitura manual.

Fontes consultadas: [Figma: limites](https://developers.figma.com/docs/figma-mcp-server/rate-limits-access/), [Figma: remoto](https://developers.figma.com/docs/figma-mcp-server/remote-server-installation/), [OpenAI: AGENTS.md](https://learn.chatgpt.com/docs/agent-configuration/agents-md), [OpenAI: MCP](https://learn.chatgpt.com/docs/extend/mcp?surface=cli).

---

## Histórico anterior — V3

Atualizado em 27/10/2026 (Brasília). Estado atual: V3 implementada e revisada; ainda não publicada.

## Objetivo e restrições

Página comercial para conquistar clientes próprios de tecnologia, apoiar credibilidade e facilitar conversas, propostas e contratações. A prospecção continua independentemente do lançamento. Serviços gerais são a prioridade; jogos ficam em segundo plano. Não inventar equipe, resultados, clientes, cases, endossos ou condições comerciais. Não expor urgência financeira. Participação e remuneração da designer em futuros contratos ainda precisam ser combinadas.

## Ambiente

- Fonte local: `/workspace/sites/gabisou-v1`.
- Repositório privado existente: `gabisou/gabisou.github.io`.
- Branch de trabalho: `codex/site-comercial-v1`; PR de revisão: https://github.com/gabisou/gabisou.github.io/pull/1.
- Site atual: https://gabisou.com/. Hospedagem e DNS ainda não confirmados. Nenhum merge, publicação, domínio ou gasto alterado.
- HTML/CSS estáticos em `dist/`, sem dependências de produção ou JavaScript de execução. Prévia sem indexação.
- `scripts/prepare_release.py --origin https://gabisou.com --output build` gera versão indexável, canonical, sitemap e dados da organização. Apenas gera arquivos; não publica.
- Logotipo local obtido do site atual. E-mail confirmado publicamente: `gabisoudev@gmail.com`; recebimento não testado.
- Instagram `https://www.instagram.com/gabisoudev/` e LinkedIn `https://www.linkedin.com/in/gabrieldevsouza/` são os destinos publicados pelo site atual.
- Sem WhatsApp: nenhum número confirmado. Sem formulário, rastreadores, CMS, banco de dados ou checkout.

## Revisão V3 — referências e mensagem

As seis referências enviadas por Gabriel foram analisadas quanto a conteúdo e navegação. Cinco sites puderam ser lidos; Studio Mirai teve leitura bloqueada e seu LinkedIn institucional foi usado como fonte complementar, com a diferença indicada. `docs/REFERENCIAS-E-MENSAGEM.md` registra fontes, comparação e limites. Não houve auditoria visual ou de desempenho dos sites de referência.

Título explícito mantido. Texto de apoio parte de três necessidades: apresentar serviços, organizar a operação, automatizar tarefas. Serviços agora vêm antes de Sobre e apresentam problema, entrega e exemplos. Sobre: “Contato direto com quem desenvolve.” Processo e convite de contato ficaram mais concretos. Nenhuma promessa de resultado, equipe fixa ou oferta adicional foi incluída. Conteúdo continua proposto, sem aprovação editorial.

Estrutura atual: início → serviços → sobre → processo → contato → rodapé. CSS, identidade, contatos e ilustração existentes preservados. Menu e rodapé acompanham a nova ordem. Prévia portátil: `gabisou-previa-v3.html`, com estilos e imagens incorporados, sem dependências externas de apresentação.

Fonte local corresponde à branch remota de revisão; o ambiente local não contém `.git`. Persistência pelo conector GitHub, preservando a árvore e usando comparação do SHA esperado. Sem merge ou deploy.

## Histórico — evidências e decisões da V2

Gabriel enviou cinco wireframes produzidos pela designer: início, sobre, projetos, serviços e rodapé. Eles ainda contêm textos e imagens de preenchimento. A direção visual da V2 parte desse trabalho, com fundo `#FAF7F4`, cabeçalho `#418CC2`, azul escuro `#2C6795`, botões arredondados e menu Sobre/Serviços/Contato. A designer não foi apresentada como funcionária e seu nome ainda não foi informado.

Estrutura da V2: início → sobre → três grupos de serviços → processo → contato → rodapé. Design de interfaces aparece explicitamente no primeiro grupo. Os outros grupos são sistemas/aplicativos/integrações e automações/IA. Não foram presumidos serviços de publicidade, branding ou gestão de redes.

Título proposto: “Sites, sistemas e automações para sua empresa.” Apoio: “Do design de interfaces ao desenvolvimento, a GABiSOU ajuda a apresentar seus serviços, organizar informações e conectar as ferramentas usadas no dia a dia.” CTA principal: “Conversar sobre meu projeto”, por e-mail.

O texto inglês antigo sobre jogos foi substituído. Não há seção vazia de Projetos: ela será incluída quando houver materiais com autoria e divulgação confirmadas. O fluxo da primeira tela permanece identificado como exemplo ilustrativo.

Rodapé: logotipo, descrição de serviços, Gabriel/Jacarepaguá/Rio de Janeiro, navegação, e-mail e Instagram secundário. Sem endereço inventado, certificações, CNPJ deduzido ou alegações legais.

`docs/CONTEUDO-PARA-DESIGN.md` reúne os textos prontos, propostas de missão/visão e requisitos para futuros cards de projetos. Missão e visão são sugestões internas; não foram adicionadas como seções ao site. Todo o conteúdo e o processo ainda são propostas editoriais, não textos aprovados por Gabriel.

## Verificação

Consultar `docs/VERIFICACAO.md` para os resultados atuais e histórico da V2. Checagens de arquivos estáticos, release, links, responsividade e contraste executadas. Limites: sem teste de recebimento de e-mail, leitor de tela, aparelhos físicos ou dados de campo. Não declarar conformidade integral WCAG.

## Escopo e continuidade

| Para lançar | Depois de ouvir compradores | Fora desta versão |
| --- | --- | --- |
| Aprovação editorial, hospedagem confirmada e autorização da publicação com ação/custo claros | Cases autorizados, refinamento dos textos, WhatsApp confirmado | Blog, checkout, membros, chatbot, painel de analytics |
| Destino de contato correto e arquivos finais revisados | Nome e apresentação pública da designer, se combinados | Preço, desconto, suporte ou Black Friday sem aprovação |

Nenhum case é obrigatório para lançar. Não reabrir triagem financeira. Próxima tarefa: revisão de Gabriel/da designer, ajustes concretos e identificação da hospedagem atual antes de preparar a ação de publicação. Não enviar mensagens à designer sem solicitação explícita.

## Medição comercial simples

Registrar manualmente data, empresa/referência, origem declarada, necessidade, próximo passo, proposta enviada, contratação e recebimento confirmado. Um clique não é conversa; conversa não é pagamento. Não publicar esses registros no site.

## Fontes

Briefing de Gabriel nesta conversa; cinco wireframes anexados; site atual inspecionado; repositório existente; referências oficiais W3C/Google listadas no relatório de verificação. O site atual confirma contatos e identidade, não comprova contratos ou resultados comerciais.
