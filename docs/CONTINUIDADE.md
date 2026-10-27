# GABiSOU — continuidade do site

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
