## ESPECIFICAÇÃO DE CASO DE USO: Gerência de Promoções

### 1 Breve Descrição

Este caso de uso é utilizado pelo dono da loja, para gerenciar as promoções da loja.

<br>

### 2 Atores

Dono da loja.

<br>

### 3 Condições Prévias

O dono da loja deve estar logado em sua conta de administrador e estar na tela de gerência do site.


<br>

### 4 Fluxo Básico de Eventos
#### 4.1 

O dono da loja clica na opção promoções.
    
<br>

#### 4.2

O dono da loja clica na opção adicionar.

<br>

#### 4.3

O dono da loja seleciona o produto que deseja botar em promoção de uma lista de produtos que não estão em promoção.

<br>

#### 4.4

O dono da loja adiciona o preço promocional do produto.

<br>

#### 4.5

O dono da loja adiciona a data em que a promoção deve acabar.

<br>

#### 4.6

O dono da loja adiciona o horário em que a promoção deve acabar.

<br>

#### 4.7

O dono da loja clica no botão de salvar.

<br>

#### 4.8

O sistema salva a promoção nova.

<br>

### 5 Fluxos Alternativos
#### 5.1 Editar promoção
##### 5.1.1

O dono da loja clica na opção promoções.

<br>

##### 5.1.2

O dono da loja seleciona a promoção que deseja alterar.

<br>

##### 5.1.3

O dono da loja edita o(s) campo(s) que deseja alterar.

<br>

##### 5.1.4

O dono da loja clica no botão de salvar.

<br>

##### 5.1.5

O sistema salva a promoção nova.

<br>

#### 5.2 Deletar conta do Usuário
##### 5.2.1

O dono da loja acessa a área de admin.

<br>

##### 5.2.2

O dono da loja clica em promoções.

<br>

##### 5.2.3

O dono da loja seleciona as promoções que deseja remover.

<br>

##### 5.2.4

O dono da loja seleciona remover no campo ação.

<br>

##### 5.2.5

O dono da loja clica no botão ir.

<br>

##### 5.2.6

O sistema remove as promoções.

<br>

### 6 Fluxo de Exceção
#### 6.1 FE1 – Promoção adicionada não contem produto, preço promocional, data ou horário

O sistema não concluirá a ação e mostrará a mensagem “Por favor, corrija os erros abaixo” identificando os campos obrigatórios com “Este campo é obrigatório”.

<br>

#### 6.2 FE2 – Nenhuma promoção selecionada

O sistema mostrará “Os itens devem ser selecionados em ordem a fim de executar ações sobre eles. Nenhum item foi modificado.” caso o dono da loja tente remover sem selecionar as promoções.

<br>

#### 6.3 FE3 – Campo obrigatório removido

O sistema não concluirá a ação e mostrará a mensagem “Por favor, corrija os erros abaixo” identificando os campos obrigatórios com “Este campo é obrigatório”.

<br>

### 7 Pós-Condições 

Todas as vezes em que um produto em promoção esteja visível na loja, deve haver o seguinte: uma comparação entre o preço antes da promoção e o preço promocional; quantas horas faltam para terminar a promoção.
Os produtos em promoção devem ser vendidos por seus preços promocionais somente até a data e o horário especificados.

<br>

### 8 Pontos de Extensão

Não se aplica.

<br>