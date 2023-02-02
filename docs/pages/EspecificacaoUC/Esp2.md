## ESPECIFICAÇÃO DE CASO DE USO: Gerenciar produtos

### 1 Breve Descrição

Este caso de uso é utilizado pelo dono da loja, para gerenciar produtos disponíveis para compra na loja.

<br>

### 2 Atores

Dono da loja.

<br>

### 3 Condições Prévias

O dono da loja deve acessar a área restrita de admin.


<br>

### 4 Fluxo Básico de Eventos
#### 4.1 Adicionar Produtos
##### 4.1.1

O dono da loja acessa a área de admin.

<br>

#### 4.1.2

O dono da loja clica na opção adicionar em products.

<br>

#### 4.1.3

O dono da loja seleciona a categoria do novo produto.

<br>

#### 4.1.4

O dono da loja adiciona o nome do produto.

<br>

#### 4.1.5

O dono da loja adiciona uma imagem ao produto.

<br>

#### 4.1.6

O dono da loja adiciona uma descrição ao produto.

<br>

#### 4.1.7

O dono da loja adiciona um preço ao produto.

<br>

#### 4.2 Editar Produto
##### 4.2.1

O dono da loja acessa a área de admin.

<br>

#### 4.2.2

O dono da loja clica na opção products.

<br>

#### 4.2.3

O dono da loja seleciona o produto que deseja alterar.

<br>

#### 4.2.4

O dono da loja edita o campo que deseja alterar.

<br>

#### 4.3 Remover Produto
##### 4.3.1

O dono da loja acessa a área de admin.

<br>

#### 4.3.2

O dono da loja clica em products.

<br>

#### 4.3.3

O dono da loja seleciona os produtos.

<br>

#### 4.3.4

O dono da loja seleciona remover no campo ação.

<br>

#### 4.3.5

O dono da loja clica no botão ir.

<br>


### 5 Fluxos Alternativos
#### 5.1 Adicionar Produtos
##### 5.1.1

O dono da loja acessa a área de admin.

<br>

#### 5.1.2

O dono da loja clica na opção adicionar em products.

<br>

#### 5.1.3

O dono da loja seleciona a categoria do novo produto.

<br>

#### 5.1.4

O dono da loja adiciona o nome do produto.

<br>

#### 5.1.5

O dono da loja adiciona uma imagem ao produto.

<br>

#### 5.1.6

O dono da loja adiciona uma descrição ao produto.

<br>

#### 5.1.7

O dono da loja adiciona um preço ao produto.

<br>

#### 5.2 Editar Produto
##### 5.2.1

O dono da loja acessa a área de admin.

<br>

#### 5.2.2

O dono da loja clica na opção products.

<br>

#### 5.2.3

O dono da loja seleciona o produto que deseja alterar.

<br>

#### 5.2.4

O dono da loja edita o campo que deseja alterar.

<br>

#### 5.3 Remover Produto
##### 5.3.1

O dono da loja acessa a área de admin.

<br>

#### 5.3.2

O dono da loja clica em products.

<br>

#### 5.3.3

O dono da loja seleciona os produtos.

<br>

#### 5.3.4

O dono da loja seleciona remover no campo ação.

<br>

#### 5.3.5

O dono da loja clica no botão ir.

<br>

### 6 Fluxo de Exceção
#### 6.1 FE1 Produto adicionado não contem nome, categoria ou preço

O sistema não concluirá a ação e mostrará a mensagem “Por favor, corrija os erros abaixo” identificando os campos obrigatórios com “Este campo é obrigatório”. 

<br>

#### 6.2 FE2 – Nenhum produto selecionado

O sistema mostrará “Os itens devem ser selecionados em ordem a fim de executar ações sobre eles. Nenhum item foi modificado, caso tentem remover sem selecionar os produtos.

<br>

#### 6.3 FE3 – Campo obrigatório removido

O sistema não concluirá a ação e mostrará a mensagem “Por favor, corrija os erros abaixo” identificando os campos obrigatórios com “Este campo é obrigatório”.

<br>

### 7 Pós-Condições 

As modificações realizadas nos produtos serão visíveis na loja.

<br>

### 8 Pontos de Extensão

Não se aplica.

<br>