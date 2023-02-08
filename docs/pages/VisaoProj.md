## VISÃO GERAL DO PROJETO

<br>

### 2.1 Organização do Projeto

| Papel                        | Atribuições                                                                                                                                          | Responsável              | Participantes                           |
| :--------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------ | --------------------------------------- |
| Desenvolvedor Front-end      | Desenvolver o produto na parte visual, manipulando os dados, para mostrar ao cliente de forma legível, e enviar ao backend de forma bem estruturada. | Lucas Sales              | Lucas Sales e Daniel Rocha              |
| DBA (Database Administrator) | Desenvolver banco de dados, tabelas, relações entre as mesmas, e demais necessidades de banco.                                                       | Leonardo Miranda         | Leonardo Miranda                        |
| Desenvolvedor Back-end       | Desenvolver conversação com o banco de dados, manusear os dados, para serem inseridos no banco, e apresentados no front-end.                         | Luiz Gustavo             | Luiz Gustavo, Bruno Kishibe, Dion Vitor |
| Cliente                      | Validar requisitos e fornecimento de dados para o Product Backlog                                                                                    | Claudio Martins Mendonça | Claudio Martins Mendonça                |

<br>

### 2.2 Planejamento das Fases e/ou Iterações do Projeto

| Sprint | Entrega                                         | Data início | Data fim |
| :----- | ----------------------------------------------- | ----------- | -------- |
| 1      | Elicitação de requisitos, definição de MVP.     | 21/11/22    | 02/12/22 |
| 2      | Criação gitpages e ambiente de desenvolvimento. | 03/12/22    | 08/12/22 |
| 3      | Desenvolvimento das US 01,03,04,05              | 08/12/22    | 22/12/22 |
| 4      | Desenvolvimento das US 16,10,09,11              | 23/12/22    | 06/01/23 |
| 5      | Desenvolvimento das US 02,14,17                 | 06/12/22    | 16/01/23 |
| 6      | Desenvolvimento das US 15,18,06                 | 17/01/23    | 30/01/23 |
| 7      | Desenvolvimento das US 07,08,12,13              | 31/01/23    | 09/02/23 |

<br>

### 2.3 Matriz de Comunicação

O telegram e o google meets serão as principais plataformas de comunicação utilizadas pela equipe.

| Descrição                                                               | Envolvidos         | Periodicidade | Produtos Gerados                                                           |
| :---------------------------------------------------------------------- | ------------------ | ------------- | -------------------------------------------------------------------------- |
| -Acompanhamento das Atividades em Andamento;                            | -Equipe do projeto | -Semanal      | -Nenhum                                                                    |
| -Acompanhamento dos Riscos, Compromissos, Ações Pendentes, Indicadores; | -Equipe do Projeto | -Quinzenal    | -Possíveis requisitos/tasks pendentes a serem resolvidos na próxima sprint |
| -Relatório do produto;                                                  | Lucas Sales        | Quinzenal     | -Ata com funcionalidades disponíveis no produto                            |
| -Alinhamento de expectativas e requisitos para próxima sprint;          | -Equipe do projeto | -Quinzenal    | -Sprint Backlog                                                            |

<br>

### 2.4 Gerenciamento de Riscos

Ao início de cada sprint, será realizada uma reunião de planejamento (planning), com a equipe de desenvolvimento, visando levantar o que deve ser feito sprint em questão, após a equipe ter isso definido, o mesmo será passado ao cliente, para que este, verifique se faz sentido estas entregas, nessa ordem, lembrando que essa será uma segunda verificação, onde a primeira, será feita na elicitação de requisitos. Ao final da sprint, uma reunião de revisão (review) será realizada juntamente ao cliente, onde serão apresentadas as entregas de valor, para que o mesmo dê um retorno, sobre suas expectativas, e se o desenvolvimento do projeto está satisfatório. Caso um risco seja identificado, podemos proceder da seguinte forma:

- **Risco leve:** Bug’s gerados por falta de atenção, não previstos, que são fáceis de arrumar, serão tratados na sprint em que foram identificados.
- **Risco mediano:** Problema com uma complexidade maior, afeta parte do sistema, mas temos uma noção de como resolvê-lo, serão orçados em conjunto do time e do cliente, podendo ser resolvidos na sprint em que foram identificados, ou na seguinte, demandando mais atenção e cuidado.
- **Risco grave:** Problema de alta complexidade, que afeta a integridade ou segurança do sistema, que a equipe não sabe como resolver. O desenvolvimento é interrompido, e a equipe se dispõe a resolver o problema o mais rápido possível, de forma eficiente, para que o desenvolvimento seja retomado, sem maiores problemas.

<br>

### 2.5 Critérios de Replanejamento

A necessidade do cliente mudar:

- Caso este cenário ocorra, precisaremos replanejar o produto, para que atenda às novas necessidades do cliente.
  A equipe não conseguir entregar o que está se propondo:
- Caso a equipe não consiga entregar o que está sendo combinado, teremos de replanejar nossa abordagem, talvez fazer mais acompanhamentos, ou diminuir a carga do backlog das sprints.
  Termos retirada do DBA do projeto:
- nisso, precisaremos utilizar uma ferramenta de ORM, para que transforme código python, em queries SQL, para que utilizemos o banco de dados de forma adequada.

## PROCESSO DE DESENVOLVIMENTO DE SOFTWARE

Após ler e estudar sobre as abordagens de Sommerville e Gupta a respeito de como escolher uma abordagem para o desenvolvimento do produto, a equipe chegou a conclusão que precisaríamos dos seguintes artefatos:

- **Iterações:** Necessária para termos um constante feedback do professor e cliente sobre o produto que estamos desenvolvendo.
- **Review ao final e planning ao início de cada iteração:** Necessária para acompanharmos nossos colegas, e compensarmos prontamente qualquer desfalque que viermos a ter.
- **Code review:** Necessário para que o produto de software seja bem feito e conciso.
- **MVP:** Necessário para guiar o desenvolvimento, e termos noção de quais requisitos agregam valor ao cliente.
- **Orçamento mínimo:** Necessário para que o cliente confie em nós inicialmente, e ele não se arrisque, assim como nós, desenvolvedores.

Alinhado com essas questões, e termos um prazo fixo, requisitos poucos conhecidos, a equipe decidiu adotar o processo de desenvolvimento SCRUM/XP, que nos permite trabalhar com iterações, mudar os requisitos de acordo com o prazo e o orçamento, e temos artefatos como as sprints, review, retrospectiva, e planning do SCRUM.
Além de utilizarmos o SAFe como estrutura de requisitos de software, utilizando temas estratégicos, épicos, features e histórias de usuário, MVP (Mínimo Produto Viável) e a URPS+ como estrutura para requisitos não funcionais.

<br>

### 3.1 Elaboração de Requisitos

| Atividade                              | Método                                                                                                                                                | Ferramenta                                     | Entrega                                                  |
| :------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------- | -------------------------------------------------------- |
| Elicitação de requisitos               | Brainstorming                                                                                                                                         | Notion                                         | Backlog do produto                                       |
| Análise dos requisitos                 | Diferenciação dos RF e RNF                                                                                                                            | Google meets                                   | Lista de RF e RNF                                        |
| Documentação de requisitos             | Estruturar requisitos em temas estratégicos, épicos, features e histórias de usuário                                                                  | Miro                                           | Backlog do produto, MVP 1 e 2, requisitos não funcionais |
| Verificação e validação dos requisitos | Validar se os requisitos ainda agregam valor ao sistema, e se estão sendo bem implementados nas suas devidas sprints, com seus critérios de aceitação | Testes de software, google meets para reuniões | Alteração ou não do backlog do produto, MVP’s e RFN      |
| Gerenciamento dos requisitos           | Durante o desenvolvimento, requisitos questionados, serão abordados juntamente ao cliente, para que os mesmos sejam refinados                         | Google meets, trello                           | Lista de requisitos a serem discutidos                   |

RF (Requisitos Funcionais) ; RNF (Requisitos Não Funcionais)

<br>

### 3.2 Análise e Design

| Atividade                         | Método         | Ferramenta | Entrega                      |
| :-------------------------------- | -------------- | ---------- | ---------------------------- |
| Elaboração do design da interface | Reunião Remota | Figma      | Protótipo de Alta Fidelidade |
| Modelagem de Banco de Dados       | Reunião Remota | DBeaver    | Design de Banco de Dados     |

<br>

### 3.3 Construção do Produto

| Atividade                    | Método          | Ferramenta             | Entrega                  |
| :--------------------------- | --------------- | ---------------------- | ------------------------ |
| Construção da interface      | Pair Programing | HTML, CSS, bootstrap   | Front-end                |
| Construção da Banco de Dados | Pair Programing | SQLite, Django, Docker | Backend e banco de dados |

## REFERÊNCIAS BIBLIOGRÁFICAS

- [Materiais Disponibilizados no Moodle](https://aprender3.unb.br/login/index.php)
