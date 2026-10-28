# GABiSOU — continuidade do site

## Estado atual — primeira parte do redesign, 28/10/2026 (Brasília)

- Objetivo: primeira versão funcional fiel ao redesign de Carol Faustino; começar apenas por cabeçalho/abertura. A V3 serve de base técnica, não de referência visual.
- Repositório: `gabisou/gabisou.github.io`; branch de trabalho `codex/figma-redesign`. O pacote de design parte do commit `178b83323eb8b9b49fc6fe2b7c98cb2ee989c5ae`. Base de implementação anterior: `857c326be11e4c335c4c508f8b4ee49995f590af` / PR #1 em rascunho.
- HTML/CSS editáveis em `dist/`; Python padrão para scripts; sem framework ou gerenciador de pacotes. Usar AGENTS.md.
- GitHub: leitura, criação de branch, commits e gravação já comprovadas nesta coordenação. Leitura de PR/CI comprovada; criação de PR ainda não exercitada nesta rodada. Não há CI executado no commit base.
- A troca de conta Figma funcionou: `gabisougpt@gmail.com`, handle Gabriel, plano Starter, assento View. A conta anterior `gabisoudev@gmail.com` foi substituída nesta conexão. Acesso real ao arquivo e contexto/captura da abertura agora comprovados.
- Arquivo: [GABiSOU-Site](https://www.figma.com/design/XYP2AAZXyTlLTNvY2OphZX/GABiSOU-Site?node-id=1-200); fileKey `XYP2AAZXyTlLTNvY2OphZX`; página única `0:1`, Website — Desktop; alvo `1:200`, 01-hero-desktop, 1920 × 1080.
- [DESIGN-HERO.md](DESIGN-HERO.md) reúne contexto extraído, geometria, textos, assets, fonte e decisões. Captura em `docs/design/hero-desktop-1920.png`; logo/arte em `dist/assets/figma/`; Inter e licença em `dist/assets/fonts/`. Não repetir a extração do Figma enquanto o design não mudar.
- Sem mobile no arquivo lido. Proposta técnica: coluna com texto/CTA antes da arte, navegação que reflow, validação 390/320 px. Não apresentar essa adaptação como design mobile aprovado.
- Arte decorativa estática exportada diretamente do Figma; manter HTML/CSS e evitar runtime React/WebGPU apenas para esse efeito sem animação/interação.
- WhatsApp ainda sem número/link confirmado; “Projetos” possui placeholders e não tem seção correspondente na V3. A prévia deve identificar recursos demonstrativos; não inventar destinos, cases ou conteúdo.
- B, segundo retorno de Gabriel: leitura GitHub e snapshot ec83e65 com 15/15 hashes conferidos; Python e check.py funcionaram. Git por terminal sem autenticação. Chrome remoto não alcançou localhost (bearer token/conexão recusada). Usar conector para persistência e encaminhar comparação visual a C se o impedimento permanecer.
- C: Windows, VS Code e Codex app/extensão informados; navegador local ainda não verificado. Sua tarefa futura é delimitada: abrir a versão de B e gerar evidências no mesmo viewport do Figma, não repetir inventário amplo.
- Checks já executados na base: 17 links, 11 IDs, 2 imagens e HTTP 200 de página/CSS/assets. Nenhuma implementação do redesign ou comparação visual do código com o Figma ocorreu ainda.
- Domínio histórico: https://gabisou.com/. Hospedagem, DNS e fluxo de publicação seguem pendentes; GitHub Pages desativado no repositório. Sem merge, publicação ou gasto autorizado nesta etapa.

### Próxima tarefa

B deve implementar cabeçalho/abertura, desktop e proposta mobile, usando os assets e a extração versionados. Conferir branch/commit antes e depois, preservar as outras seções, executar o check e produzir preview/capturas se tiver navegador funcional. Se não tiver, devolver mudanças revisáveis e handoff específico a C; estado será “implementado, aguardando conferência visual”. Só avançar às outras seções após essa comparação.

Preparação do repositório e acesso ao design concluídos; ambiente de comparação visual ainda precisa ser comprovado. No cliente Codex, distinguir carregamento automático de AGENTS.md de leitura explícita.

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
