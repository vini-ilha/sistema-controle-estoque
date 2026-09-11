# Sistema de Controle de Estoque

Projeto simples de um sistema de controle de estoque feito em Python.

## Objetivo

O sistema permite cadastrar produtos, gerir e controlar a quantidade disponível em estoque.

## Funcionalidades

- Cadastrar produtos
- Listar produtos
- Consultar produtos pelo ID
- Adicionar produtos ao estoque
- Retirar produtos do estoque
- Impedir estoque negativo
- Validar nome, preço e quantidade

## Tecnologias

- Python
- FastAPI
- Pytest
- Docker
- Git e GitHub

## Como executar

Primeiro, instale as dependências:

    py -m pip install -r requirements.txt

Depois, execute a aplicação:

    py -m uvicorn app.main:app --reload

A API poderá ser acessada em:

    http://127.0.0.1:8000/docs

## Executar os testes

Para executar os testes automatizados:

    py -m pytest -v

## Executar com Docker

Para criar a imagem:

    docker build -t estoque-api .

Para executar:

    docker run -p 8000:8000 estoque-api

Depois, acesse:

    http://127.0.0.1:8000/docs

## Estrutura do projeto

- app/ - códigos da aplicação
- testes/ - pasta de testes automatizados
- docs/ - documentação do projeto
- Dockerfile - configuração do ambiente Docker
- requirements.txt - dependências e requisitos
- AGENTS.md - instruções para o agente de IA

## Decisões do projeto

O projeto foi dividido em partes simples para facilitar os testes e a manutenção.

- produtos.py contém a classe de produto.
- estoque.py contém as regras de controle do estoque.
- main.py contém as rotas da API.

Os dados são armazenados em memória, pois o objetivo do projeto é demonstrar a estrutura da aplicação, testes, uso de agente de IA e ambiente padronizado.

## Uso de inteligência artificial

Foi utilizado o Cursor como ferramenta de auxílio no desenvolvimento.

O arquivo AGENTS.md contém as instruções utilizadas para orientar o agente sobre o projeto e suas regras.

O agente também foi utilizado para analisar a organização do projeto sem realizar alterações nos arquivos.