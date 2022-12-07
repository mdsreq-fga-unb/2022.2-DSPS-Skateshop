## _**DSPS Skateshop**_
<h1 align="center"><b>REQUISISTOS DO PRODUTO</b></h1>

<br>

### **Sumário**
 - [Backlog do produto](#backlog-do-produto)
    
 - [Requisitos Não Funcionais](#requisistos-nao-funcionais)

 - [MVPs](#mvp-produto) 
   
<br>

## Backlog do Produto

Backlog do produto é uma lista que contém os requisitos necessários para a construção de um produto de alto valor. Ou seja, trata-se de uma lista de entregas do projeto organizada em ordem de prioridade.

<br>

### Users

Os users ou usuários, são personagens fictícios representando, nesse caso, o Dono da loja e Clientes da loja, ambos com características ideais.
A seguir, temos exemplos da arquiteruta SAFe que utilizamos na elicitação de requisistos do nosso produto:

| Épico | Feature | User Story (US) |
:--------|---------|-------------|
| E01 - Produtos | FEA01 - Gerenciamento de Produtos | US01 - Eu como dono da loja, desejo poder cadastrar produtos no sistema. <br /> US02 - Eu como cliente da loja, preciso que, em caso de shapes com as mesmas especificações técnicas, eu possa escolher o desenho do shape. <br /> US03 - Eu como cliente da loja, preciso ter a opção de ver todos os produtos que a loja tem em estoque. <br /> US04 - Como dono da loja, desejo poder alterar os dados dos produtos disponíveis na loja. <br /> US05 - Como dono da loja, desejo poder deletar algum produto já cadastrado no sistema. | 
| E01 - Produtos | FEA02 - Frete, Retirada, Entrega | US06 - Eu como cliente da loja, preciso ter a opção de retirar na loja física os produtos que comprados na loja virtual. <br /> US07 - Eu como cliente da loja, preciso ter a opção de retirar na loja física os produtos que comprados na loja virtual. <br /> US08 - Eu como cliente da loja, desejo opções de frete que variam de acordo com meu CEP. <br /> US09 - Eu como cliente da loja, preciso ter a opção de comprar vários produtos de uma vez utilizando um carrinho. <br /> US10 - Eu como cliente da loja, desejo que o endereço esteja linkado ao google maps para ser mais fácil de achar a loja. |
| E02 - Gerência de Dados | FEA03 - Dados da Página | US11 - Eu como dono da loja, preciso poder editar o horário de funcionamento da minha loja. <br /> US12 - Eu como dono da loja, preciso poder editar meu número de whatsapp, meu instagram, meu youtube e meu email.  <br /> US13 - Eu como dono da loja, desejo que eu possa alterar as categorias e as subcategorias. <br /> US14 - Eu como dono da loja, preciso poder alterar as fotos e/ou vídeos dos atletas patrocinados que aparecem no banner do início da página home. <br /> US15 - Eu como dono da loja, preciso poder editar o horário de funcionamento da minha loja. <br /> US16 - Eu como dono da loja, preciso poder alterar as promoções. |
| E02 - Gerência de Dados | FEA04 - Usuários | US17 - Eu como Cliente da loja, preciso ter a opção de editar meus dados. <br /> US18 - Eu como Cliente da loja, preciso poder visualizar meu perfil com os dados cadastrados. <br /> US19 - Eu como Cliente da loja, preciso realizar o cadastro para poder comprar na loja. <br /> US20 - Eu como Cliente da loja, preciso ter a opção de desativar minha conta. |

<br>

## Requisitos Não Funcionais

Os Requisitos não-funcionais são os requisitos relacionados ao uso da aplicação em termos de desempenho, usabilidade, confiabilidade, segurança, disponibilidade, manutenibilidade e tecnologias envolvidas. Não é preciso o cliente dizer sobre eles, pois eles são características mínimas de um software de qualidade, ficando a cargo do desenvolvedor optar por atender esses requisitos ou não.

- Demonstram qualidade acerca dos serviços ou funções disponibilizadas pelo sistema. Ex.: tempo, o processo de desenvolvimento, padrões, etc.
- Surgem conforme a necessidade dos usuários, em razão de orçamento e outros fatores.
- Podem estar relacionados à confiabilidade, tempo de resposta e espaço nas mídias de armazenamento disponíveis.
- Caso ocorra falha do não atendimento a um requisito não funcional, poderá tornar todo o sistema ineficaz.

Número | Classificação | Requisitos Não Funcionais
:---------: |  :-------: |  :-------:
RNF01 | Requisitos de Legislação | Atender Lei Geral de Proteção de Dados Pessoais  (LGPD), Lei nº 13.709.
RNF02 | Requisitos de Legislação | Atender Código de Defesa do Consumidor (CDC), Lei nº 8.078.
RNF03 | Requisitos de Portabilidade |O site deve ser responsivo tanto nos celulares (mobile) quanto nos computadores (desktop).
RNF04 | Requisitos de Desempenho | O cliente deve ser avisado imediatamente após o pagamento de sua compra cair na conta da loja.
RNF05 | Requisitos de Suportabilidade | Após 1 hora de treinamento, o dono da loja deve ser capaz de alterar dados do site (como dados sobre dos produtos) sem a ajuda de desenvolvedores de software.
RNF06 | Requisitos de Interface | O processo de compra precisa ser integrado com o widget "Checkout Iframe" da plataforma GetNet.
RNF07 | Requisitos de Suportabilidade | A loja online deve atender o Brasil, com mais opções de frete para o Distrito Federal.
RNF08 | Requisitos de Implementação | Um produto pode pertencer a várias categorias e a várias subcategorias. Uma categoria de produto pode ter várias subcategorias. Uma subcategoria só pode pertencer a uma categoria. Uma subcategoria não pode ter uma subsubcategoria.

<br>

## MVPs

Minimum Viable Product (MVP).

Traduzido livremente como mínimo produto viável, é um produto, uma app, ou um site com todas as características mais básicas necessárias para ser considerado como “entregável”. Claro que, com base nos padrões atuais, dizer que algo está “entregável” com algumas poucas funcionalidades pode soar estranho, mas faz uma grande diferença para a empresa.

<br>

### MVP1

| Features | Prazo em Sprints |
|---------|----------------------|
| [FEAT01] Gerenciamento de Produtos | 05/12/2022 - 30/12/2022 |
| [FEAT04] Usuários | 05/12/2022 - 30/12/2022 |

<br>

### MVP2

| Features | Prazo em Sprints |
|---------|----------------------|
| [FEAT02] Frete, Retirada, Entrega | 02/01/2023 - 27/01/2023 |
| [FEAT03] Dados da Página | 02/01/2023 - 27/01/2023 |

<br>


  


