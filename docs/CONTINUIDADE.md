# GABiSOU — continuidade do site

Atualizado em 27/10/2026, no fuso de Brasília.

Este documento registra o estado do trabalho e permite continuá-lo em outra sessão. É documentação interna; não deve ser incluído entre os arquivos públicos do site.

## Objetivo e contexto

Produzir uma primeira versão funcional, revisada e pronta para publicação do site da GABiSOU. A página deve explicar os serviços, sustentar a credibilidade de abordagens comerciais e facilitar contatos relevantes, propostas e contratações. O site não é condição para iniciar ou continuar a prospecção.

Gabriel de Souza é desenvolvedor sênior e tech lead, em Jacarepaguá, Rio de Janeiro. A GABiSOU oferece sites, aplicativos, sistemas web, integrações, automações e soluções com IA. Clientes próprios são a prioridade; execução para agências e parcerias são alternativas secundárias. Jogos ficam em segundo plano.

Não há orçamento aprovado para anúncios, novas ferramentas ou assinaturas. A urgência comercial e financeira é contexto interno e não integra o conteúdo público. A participação da colega designer ainda precisa ser combinada; ela não deve ser apresentada como funcionária ou integrante confirmada da equipe.

## Ambiente e materiais localizados

| Item | Estado conhecido |
| --- | --- |
| Site atual | https://gabisou.com/ |
| Repositório existente | `gabisou/gabisou.github.io`, privado; a inspeção inicial encontrou apenas `README` e `.gitignore` |
| Diretório desta implementação | `/workspace/sites/gabisou-v1` |
| Arquivos públicos | `dist/`, com HTML, CSS e recursos locais; sem JavaScript em execução no navegador |
| Logo reaproveitado | `dist/assets/logo.png`, obtido do site atual |
| E-mail publicado no site atual | `gabisoudev@gmail.com` |
| Perfis publicados no site atual | Instagram `gabisoudev`; LinkedIn `/in/gabrieldevsouza/` |
| Hospedagem em uso e configuração de DNS | Não confirmadas |

Os dados encontrados no site atual foram reportados pelo agente principal durante a preparação desta versão. A presença de um e-mail no site confirma sua publicação como contato; não comprova recebimento ou acesso atual à caixa. Os perfis não precisam ser incluídos na nova página e não devem ser usados para inferir experiência, clientes ou resultados.

## Decisões da primeira versão

- Uma página principal enxuta, com meta inicial de um a dois dias de trabalho. Rever a estimativa se surgirem dependências de ambiente.
- Implementação estática em HTML e CSS, sem JavaScript em execução no navegador, CMS, banco de dados ou framework.
- Reutilizar o logotipo e a direção de cores do site existente. Os valores finais de cores e espaçamentos ficam registrados nos estilos da implementação.
- Organizar os serviços em três grupos: **sites e páginas para apresentar serviços e receber contatos**; **sistemas, aplicativos e integrações para organizar a operação**; **automações e aplicações de IA para tarefas específicas**.
- Explicar problemas e entregas antes de citar tecnologias.
- Usar o e-mail publicado no site atual como contato direto. O CTA principal deve explicitar o canal ou tornar esse destino claro.
- Não incluir WhatsApp: nenhum número foi confirmado. Não deduzir contatos nem usar números dos prospectos.
- Não incluir formulário, rastreadores ou coleta de dados nesta versão.
- Apresentar Gabriel com os fatos fornecidos pelo próprio usuário. Não apresentar experiência como funcionário como contrato da GABiSOU.
- Omitir cases, depoimentos e logotipos de clientes: não há material autorizado para esta versão. Não deixar seção vazia.
- Não incluir Black Friday, oferta, preços, descontos ou condições comerciais não aprovadas.
- Preparar e revisar os arquivos sem publicar, alterar domínio ou contratar serviços.

## Estado editorial

Os textos preparados nesta etapa são **propostas editoriais**, ainda não textos aprovados por Gabriel. A versão implementada deve ser revisada como conjunto antes do lançamento.

A estrutura editorial prevista é: primeira tela com serviço e ação principal; três grupos de serviços com exemplos de necessidades; processo curto; apresentação de Gabriel; contato. A apresentação profissional substitui uma seção de cases enquanto não houver provas autorizadas.

O processo proposto — entender a necessidade, definir escopo e proposta, desenvolver e revisar, entregar e orientar — também é uma proposta de funcionamento. Não divulgar prazos, revisões ilimitadas, manutenção incluída, suporte contínuo ou outras obrigações não combinadas.

Preservar português brasileiro natural. Não inventar equipe, anos de atuação, certificações, parceiros, escritório, métricas ou resultados. Os prospectos selecionados não são clientes. Participação em eventos não significa parceria ou endosso de Sebrae ou ACIJA.

## Escopo

| Necessário para lançar | Melhorar depois de ouvir compradores | Fora do escopo atual |
| --- | --- | --- |
| Página responsiva, texto revisado, identidade reaproveitada e contato direto correto | Ajustar explicações a partir de dúvidas recorrentes | Blog e dezenas de páginas locais |
| Navegação por teclado, foco visível, contraste e estrutura semântica | Acrescentar projetos com autoria e divulgação autorizadas | Área de membros, checkout e calculadora de orçamento |
| Título, descrição e indexabilidade verificados no destino de publicação | Acrescentar WhatsApp quando o número for confirmado | Chatbot, diagnóstico gratuito extenso e Lista VIP |
| Revisão de links, imagens, ausência de dados fictícios e funcionamento em celular e desktop | Detalhar um serviço que demonstre demanda real | Animações complexas e demonstrações extensas |
| Hospedagem identificada e publicação autorizada com ação e custo claros | Medição adicional, se houver necessidade concreta e configuração aprovada | Campanha de Black Friday sem oferta e prazo aprovados |

## Verificação e pendências

Resultados já informados pelo agente principal nesta sessão:

- [x] Scripts de verificação `check` e de preparação `release` executados com sucesso.
- [x] Ausência de rolagem horizontal indevida verificada em quatro larguras de tela.
- [x] Link de salto para o conteúdo principal testado.

O ambiente de execução ficou temporariamente indisponível durante a última etapa de revisão e voltou com os arquivos intactos. A interrupção não invalida os testes concluídos, mas os itens abaixo ainda precisam de fechamento e registro concreto:

- [ ] Concluir a última revisão visual e de navegação em celular e desktop.
- [ ] Concluir a verificação do contato, incluindo destino exato do e-mail e comportamento do link.
- [ ] Registrar a revisão final de teclado, foco, contraste, rótulos e textos alternativos com WCAG 2.2 como referência, além do link de salto já testado.
- [ ] Registrar a revisão editorial final: conteúdo, autoria e ausência de placeholders públicos ou condições comerciais não aprovadas.
- [ ] Registrar somente medições de carregamento e desempenho efetivamente realizadas; distinguir laboratório de métricas reais e não inventar pontuações.
- [ ] Verificar a política de indexação e os metadados no destino final de publicação.
- [ ] Confirmar hospedagem atual e caminho de publicação antes de substituir qualquer conteúdo existente.
- [ ] Obter aprovação da versão e da ação de publicação; declarar eventual custo antes da autorização.
- [ ] Se Gabriel desejar um teste real de recebimento de e-mail, combiná-lo explicitamente. O teste não foi realizado e a existência de um link `mailto:` não o substitui.

Não houve publicação. Não há formulário ou WhatsApp a testar nesta versão. Não declarar conformidade integral de acessibilidade com base apenas em automação. Os resultados acima se limitam às verificações concluídas e não substituem a revisão final.

## Medição comercial simples

Registrar manualmente apenas informações necessárias para acompanhar oportunidades. Não inserir dados pessoais sensíveis ou detalhes de clientes nos arquivos públicos. Um clique no contato não comprova conversa, proposta, contratação ou pagamento.

| Data | Empresa ou referência | Origem declarada | Necessidade e contato relevante | Proposta | Contratação | Recebimento confirmado |
| --- | --- | --- | --- | --- | --- | --- |
| — | — | Site, indicação, prospecção ou outra | Resumo e próximo passo | Data ou pendente | Data ou pendente | Data ou pendente |

Contato relevante significa uma conversa com necessidade identificável e possibilidade de próximo passo. Proposta significa proposta efetivamente enviada. Contratação e recebimento devem ser registrados separadamente, conforme confirmação real. O site pode apoiar uma oportunidade cuja origem foi a prospecção; não atribuir toda contratação ao site sem evidência.

## Fontes e limites

- Briefing do usuário nesta conversa: contexto profissional, oferta de serviços, prioridades, restrições e critérios de publicação.
- Site atual, https://gabisou.com/: logotipo, direção visual e contatos públicos, conforme inspeção do agente principal.
- Inspeção do repositório privado `gabisou/gabisou.github.io`: estado inicial relatado acima; não demonstra por si só onde o domínio está hospedado.
- WCAG 2.2: referência de acessibilidade solicitada pelo usuário, https://www.w3.org/TR/WCAG22/. Esta menção não representa auditoria ou certificação.

## Próxima tarefa

Preservar os arquivos em uma branch de revisão, concluir os itens finais de QA e apresentar a versão revisável a Gabriel. Depois, resolver somente os bloqueios reais de lançamento: ajustes solicitados, hospedagem e autorização para a ação concreta de publicação. Não reabrir a triagem financeira nem condicionar a prospecção ao site.

Trabalhos rotineiros seguem em profundidade econômica. Recomendar profundidade máxima apenas se uma dependência, falha persistente ou decisão conflitante justificar o esforço; não alegar alterar o modo da plataforma.
