# Especificação do Sistema

## 1. Descrição do problema
O sistema tem como objetivo controlar produtos de um estoque de forma simples.
O usuário pode cadastrar produtos, consultar os produtos cadastrados e realizar entradas e saídas de estoque.
O sistema também possui validações para evitar dados inválidos e impedir que a quantidade disponível fique negativa.

## 2. Requisitos funcionais
- RF01 - Cadastrar um produto.
- RF02 - Listar os produtos cadastrados.
- RF03 - Buscar um produto pelo ID.
- RF04 - Adicionar quantidade ao estoque.
- RF05 - Retirar quantidade do estoque.
- RF06 - Impedir que o estoque fique negativo.
- RF07 - Validar os dados informados no cadastro e nas movimentações.

## 3. Requisitos não funcionais
- RNF01 - O sistema deve ser desenvolvido em Python.
- RNF02 - A API deve utilizar FastAPI.
- RNF03 - O sistema deve possuir testes automatizados utilizando Pytest.
- RNF04 - O projeto deve poder ser executado utilizando Docker.
- RNF05 - O código deve ser simples e organizado para facilitar a manutenção.

## 4. Regras de negócio
- RN01 - O nome do produto não pode ficar vazio.
- RN02 - O preço do produto deve ser maior que zero.
- RN03 - A quantidade inicial não pode ser negativa.
- RN04 - A quantidade de entrada deve ser maior que zero.
- RN05 - A quantidade de saída deve ser maior que zero.
- RN06 - Não é permitido retirar uma quantidade maior que a disponível no estoque.
- RN07 - Cada produto deve possuir um ID único.
- RN08 - Ao buscar um produto inexistente, o sistema deve informar que o produto não foi encontrado.

## 5. Entradas e saídas

### Cadastro de produto
Entrada:
- nome
- preço
- quantidade inicial

Saída:
- ID do produto
- nome
- preço
- quantidade em estoque

### Entrada de estoque
Entrada:
- ID do produto
- quantidade

Saída:
- produto atualizado com a nova quantidade em estoque

### Saída de estoque
Entrada:
- ID do produto
- quantidade

Saída:
- produto atualizado com a nova quantidade em estoque

Caso a quantidade solicitada seja maior que a disponível, a operação deve ser recusada.

## 6. API
As principais rotas da aplicação são:
- `POST /produtos` - cadastrar produto
- `GET /produtos` - listar produtos
- `GET /produtos/{id}` - buscar produto
- `POST /produtos/{id}/entrada` - adicionar estoque
- `POST /produtos/{id}/saida` - retirar estoque

## 7. Componentes
O sistema foi dividido em componentes simples:
- `produtos.py` - representa os produtos.
- `estoque.py` - contém as regras de controle e movimentação do estoque.
- `main.py` - disponibiliza as funcionalidades através da API.
- `test_estoque.py` - contém os testes automatizados.

Essa divisão facilita a manutenção e permite testar as regras do estoque de forma independente da API.

## 8. Testes
Foram realizados testes automatizados utilizando Pytest.
O comando utilizado foi:

    py -m pytest -v

Resultado da execução:
- 8 testes executados
- 8 testes aprovados
- 0 testes reprovados

Os testes verificaram cadastro de produtos, validação de dados, entrada e saída de estoque, tentativa de retirada maior que o estoque e busca por produto inexistente.

O relatório da execução está disponível em:
`docs/relatorio-testes.txt`

## 9. Refinamento após testes
Após a implementação, os testes foram executados para verificar se as principais regras definidas na especificação estavam funcionando corretamente.

A execução apresentou 8 testes aprovados e nenhum teste reprovado.

Também foi realizada uma verificação da aplicação utilizando Docker e da API através da documentação do FastAPI.

Com base nessas verificações, foi confirmado que as funcionalidades principais estavam de acordo com a especificação inicial.