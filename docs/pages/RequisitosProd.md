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

| Épico                   | Feature                           | User Story (US)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| :----------------------- | --------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | Critérios de Aceitação | ----------------------------------------------------------------|
| E01 - Produtos           | FEA01 - Gerenciamento de Produtos | US01 - Eu como dono da loja, desejo poder Cadastrar produtos no sistema para que eventualmente eu possa disponibilizá-los para o público.<br /> US02 - Eu como cliente da loja, preciso que eu possa escolher o desenho do shape para atender minhas necessidades. <br /> US03 - Eu como cliente da loja, preciso ter a opção de ver todos os produtos que a loja tem em estoque para que eu possa vê-los de modo mais amplo e rápido<br /> US04 - Como dono da loja, desejo poder alterar os dados dos produtos disponíveis na loja para que eu possa consertar ou atualizar dados dos produtos. <br /> US05 - Como dono da loja, desejo poder deletar algum produto já cadastrado no sistema para que eu possa ter um bom controle de produtos da minha loja.| (CA)US01 - Somente o dono da loja pode cadastrar novos produtos que serão vendidos na loja; Devem ser preenchidos todos os campos corretamente. Inclusive enviar fotos. <br /> (CA)US02 - deve ter um campo para escolher a variação dos desenhos de shapes; Deve possuir imagens com os desenhos a serem escolhidos.<br /> CA(US03) - Deverá ter uma aba com todos os produtos disponíveis da loja, juntando todas as categorias. <br/> CA(US04) - Somente o dono da loja pode editar os dados de um produto. <br /> (CA)US05 - Somente o dono da loja pode deletar um produto; O produto não deve ser apagado do banco de Dados, deve ser apenas desabilitado para as vendas.    |
| E01 - Produtos           | FEA02 - Frete, Retirada, Entrega  | US06 - Eu como cliente da loja, preciso ter a opção de retirar na loja física os produtos que comprados na loja virtual para que eu possa estar adquirindo meu produto mais rapidamente. <br /> US07 - Eu como cliente da loja, desejo opções de frete que variam de acordo com meu CEP para que eu possa ver quanto de frete eu irei pagar. <br /> US08 - Eu como cliente da loja, preciso ter a opção de comprar vários produtos de uma vez utilizando um carrinho para que as compras na loja fiquem mais rápidas e dinâmicas. <br /> US09 - Eu como cliente da loja, desejo que o endereço esteja linkado ao google maps para ser mais fácil de achar a loja.|(CA)US06 - Antes do pagamento final da compra deve ser selecionado se o cliente deseja buscar o produto que está sendo comprado, ou se irá pagar o frete para recebimento no endereço selecionado. <br /> (CA)US07 - Deverá ter uma seção de fretes disponíveis para cada região.<br /> CA(US08) - O carrinho de compras só pode ser fechado se possuir um ou mais produtos. <br/> CA(US09) - Deverá possuir uma área de endereço atualizado.                    |
| E02 - Gerência de Dados | FEA03 - Dados da Página          | US10 - Eu como dono da loja, preciso poder editar o horário de funcionamento da minha loja para que o cliente não venha buscar o produto em um horário de não funcionamento.<br /> US11 - Eu como dono da loja, preciso poder editar meu número de whatsapp, meu instagram, meu youtube e meu email para que eu possa manter meus clientes atualizados sobre as formas de contato comigo  <br /> US12 - Eu como dono da loja, desejo que eu possa alterar as categorias para manter a organização adequada da loja. <br /> US13 - Eu como dono da loja, preciso poder alterar as fotos e/ou vídeos dos atletas patrocinados que aparecem no banner da homepage para que eu possa manter meus clientes atualizados dos atletas patrocinados. <br /> US14 - Eu como dono da loja, preciso da opção de editar o endereço da minha loja para manter meus clientes atualizados caso eu mude de local. <br /> US15 - Eu como dono da loja, preciso poder Alterar as promoções para promover mais dinâmica de vendas com os meus clientes. <br /> US16 - Eu como dono da loja, desejo poder editar a seção de perguntas frequentes para poupar meu tempo na hora de atender os clientes. | CA(US010) - Somente o dono da Loja pode Editar os dados referentes a loja; Assim que alterados devem ser modificados imediatamente no site. <br /> CA(US11) - Somente o dono da Loja pode Editar os dados referentes a loja; Assim que alterados devem ser modificados imediatamente no site.  <br/> CA(US12) - Somente o dono da loja pode editar as categorias dos produtos. <br /> CA(US13) - Deverá possuir uma área própria para alterar patrocinados da loja; Somente o dono da loja poderá alterar esses dados. <br /> CA(US14) - Somente o dono da Loja pode Editar os dados referentes a loja; Assim que alterados devem ser modificados imediatamente no site. <br /> CA(US15) - Somente o dono da loja poderá alterar as promoções; Deverá possuir uma comparação entre o preço original e o promocional. <br /> CA(US16) -  Somente o dono da Loja pode Editar os dados referentes a loja; As perguntas frequentes devem ser alteradas rapidamente com base no número de perguntas feitas.                    |
| E02 - Gerência de Dados | FEA04 - Usuários                 | US17 - Eu como Cliente da loja, preciso ter a opção de editar meus dados para não ter dados errados na minha conta.<br /> US18 - Eu como Cliente da loja, preciso poder visualizar meu perfil com os dados cadastrados para caso eu queira alterá-los. <br /> US19 - Eu, como cliente da loja, preciso realizar o cadastro para poder comprar na loja. <br /> US20 - Eu como Cliente da loja, preciso ter a opção de desativar minha conta para caso eu não queira mais comprar na loja. | CA(US17) - Qualquer dado pode ser alterado separadamente; A alteração de e-mail ou telefone deve ser confirmado pelo e-mail previamente cadastrado. <br /> CA(US18) - Deverá ter um botão para acessar o perfil do usuário; Deverá ter uma página com todos os dados cadastrados do usuário<br /> CA(US19) - Todos os campos devem ser preenchidos, respeitando o tipo de dado definido; Não podem ser registrados mais de um usuário com o mesmo e-mail. <br/> CA(US20) - Deve haver uma opção de deleção da conta para o cliente que esteja logado. É preciso haver uma mensagem de confirmação para tal ação.                   |

<br>

## Requisitos Não Funcionais

Os Requisitos não-funcionais são os requisitos relacionados ao uso da aplicação em termos de desempenho, usabilidade, confiabilidade, segurança, disponibilidade, manutenibilidade e tecnologias envolvidas. Não é preciso o cliente dizer sobre eles, pois eles são características mínimas de um software de qualidade, ficando a cargo do desenvolvedor optar por atender esses requisitos ou não.

- Demonstram qualidade acerca dos serviços ou funções disponibilizadas pelo sistema. Ex.: tempo, o processo de desenvolvimento, padrões, etc.
- Surgem conforme a necessidade dos usuários, em razão de orçamento e outros fatores.
- Podem estar relacionados à confiabilidade, tempo de resposta e espaço nas mídias de armazenamento disponíveis.
- Caso ocorra falha do não atendimento a um requisito não funcional, poderá tornar todo o sistema ineficaz.

| Número |        Classificação        |                                                                                                         Requisitos Não Funcionais                                                                                                         |
| :-----: | :---------------------------: | :-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------: |
|  RNF01  |  Requisitos de Legislação  |                                                                                 Atender Lei Geral de Proteção de Dados Pessoais  (LGPD), Lei nº 13.709.                                                                                 |
|  RNF02  |  Requisitos de Legislação  |                                                                                        Atender Código de Defesa do Consumidor (CDC), Lei nº 8.078.                                                                                        |
|  RNF03  |  Requisitos de Usabilidade  |                                                                         O site deve ser responsivo tanto nos celulares (mobile) quanto nos computadores (desktop).                                                                         |
|  RNF04  |   Requisitos de Desempenho   |                                                                       O cliente deve ser avisado imediatamente após o pagamento de sua compra cair na conta da loja.                                                                       |
|  RNF05  | Requisitos de Suportabilidade |                                       Após 1 hora de treinamento, o dono da loja deve ser capaz de alterar dados do site (como dados sobre dos produtos) sem a ajuda de desenvolvedores de software.                                       |
|  RNF06  |    Requisitos de Implementação    |                                                                       O processo de compra precisa ser integrado com o widget "Checkout Iframe" da plataforma GetNet.                                                                       |
|  RNF07  | Requisitos de Suportabilidade |                                                                          A loja online deve atender o Brasil, com mais opções de frete para o Distrito Federal.                                                                          |
|  RNF08  | Requisitos de Implementação | Um produto pode pertencer a várias categorias e a várias subcategorias. Uma categoria de produto pode ter várias subcategorias. Uma subcategoria só pode pertencer a uma categoria. Uma subcategoria não pode ter uma subsubcategoria. |

<br>

## MVPs

Minimum Viable Product (MVP).

Traduzido livremente como mínimo produto viável, é um produto, uma app, ou um site com todas as características mais básicas necessárias para ser considerado como “entregável”. Claro que, com base nos padrões atuais, dizer que algo está “entregável” com algumas poucas funcionalidades pode soar estranho, mas faz uma grande diferença para a empresa.

<br>

### MVP1

| Features                           | Prazo em Sprints        |
| ---------------------------------- | ----------------------- |
| [FEAT01] Gerenciamento de Produtos | 05/12/2022 - 10/01/2023 |
| [FEAT04] Usuários                  | 05/12/2022 - 10/01/2023 |

<br>

### MVP2

| Features                          | Prazo em Sprints        |
| --------------------------------- | ----------------------- |
| [FEAT02] Frete, Retirada, Entrega | 10/01/2023 - 06/02/2023 |
| [FEAT03] Dados da Página          | 10/01/2023 - 06/02/2023 |

<br>
