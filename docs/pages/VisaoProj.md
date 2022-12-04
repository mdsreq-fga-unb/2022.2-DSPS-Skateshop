## VISÃO GERAL DO PROJETO

<br>

### 2.1 Organização do Projeto

| Papel | Atribuições | Responsável | Participantes |
:--------|-------------|-------------|---------------|
| Desenvolvedor Front-end | Desenvolver o produto na parte visual, manipulando os dados, para mostrar ao cliente de forma legível, e enviar ao backend de forma bem estruturada. | Lucas Sales | Lucas Sales e Daniel Rocha |
| DBA (Database Administrator) | Desenvolver banco de dados, tabelas, relações entre as mesmas, e demais necessidades de banco. | Leonardo Miranda | Leonardo Miranda |
| Desenvolvedor Back-end | Desenvolver conversação com o banco de dados, manusear os dados, para serem inseridos no banco, e apresentados no front-end. | Luiz Gustavo | Luiz Gustavo, Bruno Kishibe, Dion Vitor |
| Cliente | Validar requisitos e fornecimento de dados para o Product Backlog | Claudio Martins Mendonça | Claudio Martins Mendonça |

<br>

### 2.2 Planejamento das Fases e/ou Iterações do Projeto

| Sprint | Entrega | Data início | Data fim |
:--------|---------|-------------|----------|
| 1 | Elicitaçao de requisitos, definição de MVP, configuração de ambiente de desenvolvimento | 21/11/22 | 02/12/22 |
| 2 | MVP e Planejamento do Projeto | 05/12/22 | 16/12/22 |
| 3 | Desenvolvimento de funcionalidades a serem definidas | 19/12/22 | 30/12/22 |
| 4 | Desenvolvimento de funcionalidades a serem definidas | 02/01/23 | 13/01/23 |
| 5 | Desenvolvimento de funcionalidades a serem definidas | 16/01/23 | 27/01/23 |
| 6 | Desenvolvimento de funcionalidades a serem definidas, configuração do ambiente de produção de deploy | 30/01/23 | 10/02/23 |
| Review | Tratamento de últimos erros, e ajustes mínimos | 13/02/23 | 16/02/23 |

<br>

### 2.3 Matriz de Comunicação

O telegram e o Discord serão as principais plataformas de comunicação utilizadas pela equipe.

| Descrição | Envolvidos | Periodicidade | Produtos Gerados |
:-----------|------------|---------------|------------------|
| -Acompanhamento das Atividades em Andamento; 
-Acompanhamento dos Riscos, Compromissos, Ações Pendentes, Indicadores; | -Equipe do Projeto | -Quinzenal | -Possíveis requisitos/tasks pendentes a serem resolvidos na próxima sprint |
| -Relatório do produto;
-Parecer do estado atual do produto;
-Alinhamento de expectativas e requisitos para próxima sprint; | -Equipe do projeto
-Cliente | -Quinzenal | -Ata de reunião
-Lista de requisitos candidatos a estar no backlog da próxima sprint |
| -Comunicar situação do projeto | -Equipe do projeto
-Professor | -Semanal | -Relatório de situação do projeto |

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
<br>
A equipe não conseguir entregar o que está se propondo:
- Caso a equipe não consiga entregar o que está sendo combinado, teremos de replanejar nossa abordagem, talvez fazer mais acompanhamentos, ou diminuir a carga do backlog das sprints.
<br>
Termos retirada do DBA do projeto:
- nisso, precisaremos utilizar uma ferramenta de ORM, para que transforme código python, em queries SQL, para que utilizemos o banco de dados de forma adequada.
<br>

## REFERÊNCIAS BIBLIOGRÁFICAS
- [Materiais Disponibilizados no Moodle](https://aprender3.unb.br/login/index.php)