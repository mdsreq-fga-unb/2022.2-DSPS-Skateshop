## _**DSPS Skateshop**_

<h1 align="center"><b>REQUISITOS DO PRODUTO</b></h1>

<br>

### **Sumário**

- [_**DSPS Skateshop**_](#dsps-skateshop)
  - [**Sumário**](#sumário)
- [Backlog do Produto](#backlog-do-produto)
  - [Papel de usuário](#papel-de-usuário)
- [Requisitos Não Funcionais](#requisitos-não-funcionais)
- [MVPs](#mvps)
  - [MVP1](#mvp1)
  - [MVP2](#mvp2)

<br>

## Backlog do Produto

Backlog do produto é uma lista que contém os requisitos necessários para a construção de um produto de alto valor. Ou seja, trata-se de uma lista de entregas do projeto organizada em ordem de prioridade.

<br>

### Papel de usuário

Há o papel "dono da loja" e o papel "cliente da loja". O dono da loja é responsável pela manutenção do estoque loja online. O cliente da loja é quem compra produtos da loja online.

| Épicos (E)              | Features (FEA)                    | User Stories (US)                                                                                                                                                                                                          | Critérios de Aceitação                                                                                                                                                                                                                                                                                                          |
| ----------------------- | --------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| E01 - Produtos          | FEA01 - Gerenciamento de Produtos | US01 - Eu, como dono da loja, desejo poder cadastrar produtos no sistema para que eventualmente eu possa disponibilizá-los para o público.                                                                                 | Somente o dono da loja pode cadastrar novos produtos que serão vendidos na loja; Estes atributos do produto devem ser obrigatórios: nome do produto, preço e fotos (pelo menos, 1 foto). E, este outro campo deve ser opcional para o dono da loja: descrição.                                                                  |
|                         |                                   | US02 - Eu, como cliente da loja, preciso escolher o desenho do shape para atender minhas necessidades.                                                                                                                     | Deve ter um campo que possibilite a escolha do desenho do shape; Deve possuir imagens com os desenhos a serem escolhidos.                                                                                                                                                                                                       |
|                         |                                   | US03 - Eu, como cliente da loja, preciso ter a opção de ver todos os produtos que a loja tem em estoque para que eu tenha uma rápida visão geral dos produtos da loja.                                                     | Deverá ter uma aba com todos os produtos disponíveis da loja, juntando todas as categorias.                                                                                                                                                                                                                                     |
|                         |                                   | US04 - Eu, como dono da loja, desejo poder alterar os dados dos produtos disponíveis na loja para que eu possa consertar ou atualizar dados dos produtos.                                                                  | Somente o dono da loja pode editar os dados de um produto.                                                                                                                                                                                                                                                                      |
|                         |                                   | US05 - Eu, como dono da loja, desejo poder deletar algum produto já cadastrado no sistema para que eu possa ter um bom controle de produtos da minha loja.                                                                 | Somente o dono da loja pode deletar um produto; O produto não deve ser apagado do banco de dados, deve ser apenas desabilitado para as vendas.                                                                                                                                                                                  |
|                         | FEA02 - Frete, Retirada e Entrega | US06 - Eu, como cliente da loja, preciso ter a opção de retirar na loja física os produtos que comprados na loja virtual para que eu possa estar adquirindo meu produto mais rapidamente.                                  | Antes do pagamento final da compra deve ser selecionado se o cliente deseja buscar o produto que está sendo comprado, ou se irá pagar o frete para recebimento no endereço selecionado.                                                                                                                                         |
|                         |                                   | US07 - Eu, como cliente da loja, desejo opções de frete que variam de acordo com meu CEP para que eu possa ver quanto de frete eu irei pagar.                                                                              | O preço do frete deve ser calculado a partir do CEP do cliente.                                                                                                                                                                                                                                                                 |
|                         |                                   | US08 - Eu, como cliente da loja, preciso ter a opção de comprar vários produtos de uma vez utilizando um carrinho para que eu não precise comprar um produto de cada vez e para que eu possa, talvez, economizar no frete. | O carrinho de compras só pode ser fechado se possuir um ou mais produtos.                                                                                                                                                                                                                                                       |
|                         |                                   | US09 - Eu, como cliente da loja, desejo que o endereço esteja linkado ao google maps para ser mais fácil de achar a loja.                                                                                                  | Deverá possuir uma área de endereço atualizado.                                                                                                                                                                                                                                                                                 |
| E02 - Gerência de Dados | FEA03 - Dados da Página           | US10 - Eu, como dono da loja, preciso poder editar o horário de funcionamento da minha loja para que clientes e potenciais clientes, sem precisar me fazer perguntas sobre horário, possam se organizar para vir à loja.   | Somente o dono da loja pode editar os dados referentes a loja; Assim que alterados devem ser modificados imediatamente no site.                                                                                                                                                                                                 |
|                         |                                   | US11 - Eu, como dono da loja, preciso poder editar meu número de whatsapp, meu instagram, meu youtube e meu email para que os clientes saibam como me contatar e para que conheçam meus outros meios de comunicação.       | Somente o dono da loja pode editar tais dados; Assim que alterados devem ser modificados imediatamente no site.                                                                                                                                                                                                                 |
|                         |                                   | US12 - Eu, como dono da loja, desejo que eu possa alterar as categorias para manter a organização adequada da loja.                                                                                                        | Somente o dono da loja pode editar as categorias dos produtos.                                                                                                                                                                                                                                                                  |
|                         |                                   | US13 - Eu, como dono da loja, preciso poder alterar as fotos e/ou vídeos dos atletas patrocinados que aparecem no banner da homepage para que eu possa manter meus clientes atualizados dos atletas patrocinados.          | Deverá possuir uma área própria para alterar patrocinados da loja; Somente o dono da loja poderá alterar esses dados.                                                                                                                                                                                                           |
|                         |                                   | US14 - Eu, como dono da loja, preciso da opção de editar o endereço da minha loja para manter meus clientes atualizados caso eu mude de local.                                                                             | Somente o dono da loja pode editar o endereço da loja; Assim que alterado deve ser modificado imediatamente no site.                                                                                                                                                                                                            |
|                         |                                   | US15 - Eu, como dono da loja, preciso poder alterar as promoções para promover mais dinâmica de vendas com os meus clientes.                                                                                               | Somente o dono da loja poderá alterar as promoções; Todas as promoções devem aparecer na homepage; Na homepage, em cada produto em promoção mostrado, deve haver uma comparação entre o preço original e o promocional; Na página de cada produto, deve haver uma comparação entre o preço original e o promocional.            |
|                         |                                   | US16 - Eu, como dono da loja, desejo poder editar a seção de perguntas frequentes para poupar meu tempo na hora de atender os clientes.                                                                                    | Somente o dono da loja pode editar as perguntas frequentes e suas respostas.                                                                                                                                                                                                                                                    |
|                         | FEA04 - Usuários                  | US17 - Eu, como cliente da loja, preciso ter a opção de editar meus dados para não ter dados errados nem dados desatualizados na minha conta.                                                                              | Exceto CPF e data de nascimento, qualquer dado pode ser alterado separadamente; O CPF e a data de nascimento devem ser imutáveis; Em caso de alteração de telefone celular, o número novo deve ser validado por meio de SMS; Em caso de alteração do endereço de email, o email novo deve ser validado sem usar o email antigo. |
|                         |                                   | US18 - Eu, como cliente da loja, preciso poder visualizar meu perfil com os dados cadastrados para caso eu queira alterá-los.                                                                                              | Deverá ter um botão para acessar o perfil do usuário; Deverá ter uma página com todos os dados cadastrados do usuário.                                                                                                                                                                                                          |
|                         |                                   | US19 - Eu, como cliente da loja, preciso realizar o cadastro para poder comprar na loja.                                                                                                                                   | Os atributos do usuário a ser cadastrado são CPF ou CNPJ, data de nascimento, email e telefone celular; Com exceção do campo do telefone celular, todos os campos devem ser preenchidos; Não podem haver usuários com mesmo email, nem com mesmo CPF e nem com mesmo CNPJ.                                                      |
|                         |                                   | US20 - Eu, como cliente da loja, preciso ter a opção de desativar minha conta para caso eu não queira mais a minha conta ou os meus dados na loja virtual.                                                                 | Deve haver uma opção de deleção da conta para o cliente que esteja logado. É preciso haver uma mensagem de confirmação para tal ação.                                                                                                                                                                                           |

## Requisitos Não Funcionais

Os Requisitos não-funcionais são os requisitos relacionados ao uso da aplicação em termos de desempenho, usabilidade, confiabilidade, segurança, disponibilidade, manutenibilidade e tecnologias envolvidas. Não é preciso o cliente dizer sobre eles, pois eles são características mínimas de um software de qualidade, ficando a cargo do desenvolvedor optar por atender esses requisitos ou não.

- Demonstram qualidade acerca dos serviços ou funções disponibilizadas pelo sistema. Ex.: tempo, o processo de desenvolvimento, padrões, etc.
- Surgem conforme a necessidade dos usuários, em razão de orçamento e outros fatores.
- Podem estar relacionados à confiabilidade, tempo de resposta e espaço nas mídias de armazenamento disponíveis.
- Caso ocorra falha do não atendimento a um requisito não funcional, poderá tornar todo o sistema ineficaz.

| Número |         Classificação         |                                                                   Requisitos Não Funcionais                                                                    |
| :----: | :---------------------------: | :------------------------------------------------------------------------------------------------------------------------------------------------------------: |
| RNF01  |   Requisitos de Legislação    |                                             Atender Lei Geral de Proteção de Dados Pessoais (LGPD), Lei nº 13.709.                                             |
| RNF02  |   Requisitos de Legislação    |                                                  Atender Código de Defesa do Consumidor (CDC), Lei nº 8.078.                                                   |
| RNF03  |   Requisitos de Usabilidade   |                                   O site deve ser responsivo tanto nos celulares (mobile) quanto nos computadores (desktop).                                   |
| RNF04  |   Requisitos de Desempenho    |                            O cliente deve ser avisado, em questão de minutos, após o pagamento de sua compra cair na conta da loja.                            |
| RNF05  |   Requisitos de Usabilidade   | Após 1 hora de treinamento, o dono da loja deve ser capaz de alterar dados do site (como dados sobre dos produtos) sem a ajuda de desenvolvedores de software. |
| RNF06  |  Requisitos de Implementação  |                                O processo de compra precisa ser integrado com o widget "Checkout Iframe" da plataforma GetNet.                                 |
| RNF07  | Requisitos de Suportabilidade |                                                              A loja online deve atender o Brasil.                                                              |
| RNF08  |  Requisitos de Implementação  |                                                         Um produto pode pertencer a várias categorias.                                                         |

<br>

## MVPs

Minimum Viable Product (MVP).

Traduzido livremente como mínimo produto viável, é um produto, uma app, ou um site com todas as características mais básicas necessárias para ser considerado como “entregável”. Claro que, com base nos padrões atuais, dizer que algo está “entregável” com algumas poucas funcionalidades pode soar estranho, mas faz uma grande diferença para a empresa.

<br>

### MVP1

| Histórias de Usuário | Prazo em Sprints        |
| -------------------- | ----------------------- |
| E01 - FEA01 - US01   | 05/12/2022 - 10/01/2023 |
| E01 - FEA01 - US03   | 05/12/2022 - 10/01/2023 |
| E01 - FEA01 - US04   | 05/12/2022 - 10/01/2023 |
| E01 - FEA01 - US05   | 05/12/2022 - 10/01/2023 |
| E01 - FEA02 - US09   | 05/12/2022 - 10/01/2023 |
| E02 - FEA03 - US10   | 05/12/2022 - 10/01/2023 |
| E02 - FEA03 - US11   | 05/12/2022 - 10/01/2023 |
| E02 - FEA03 - US12   | 05/12/2022 - 10/01/2023 |
| E02 - FEA03 - US14   | 05/12/2022 - 10/01/2023 |

<br>

### MVP2

| Histórias de Usuário | Prazo em Sprints        |
| -------------------- | ----------------------- |
| E01 - FEA01 - US02   | 10/01/2023 - 06/02/2023 |
| E01 - FEA02 - US06   | 10/01/2023 - 06/02/2023 |
| E01 - FEA02 - US07   | 10/01/2023 - 06/02/2023 |
| E01 - FEA02 - US08   | 10/01/2023 - 06/02/2023 |
| E02 - FEA03 - US13   | 10/01/2023 - 06/02/2023 |
| E02 - FEA03 - US15   | 10/01/2023 - 06/02/2023 |
| E02 - FEA03 - US16   | 10/01/2023 - 06/02/2023 |
| E02 - FEA04 - US17   | 10/01/2023 - 06/02/2023 |
| E02 - FEA04 - US18   | 10/01/2023 - 06/02/2023 |
| E02 - FEA04 - US19   | 10/01/2023 - 06/02/2023 |
| E02 - FEA04 - US20   | 10/01/2023 - 06/02/2023 |

<br>
