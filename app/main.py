from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

from app.estoque import Estoque


app = FastAPI()

estoque = Estoque()


class ProdutoEntrada(BaseModel):
    nome: str
    preco: float
    quantidade: int


class Quantidade(BaseModel):
    quantidade: int


@app.post("/produtos")
def cadastrar_produto(produto: ProdutoEntrada):
    try:
        novo_produto = estoque.cadastrar_produto(
            produto.nome,
            produto.preco,
            produto.quantidade
        )

        return {
            "id": novo_produto.id,
            "nome": novo_produto.nome,
            "preco": novo_produto.preco,
            "estoque": novo_produto.estoque
        }

    except ValueError as erro:
        raise HTTPException(status_code=400, detail=str(erro))


@app.get("/produtos")
def listar_produtos():
    return estoque.listar_produtos()


@app.get("/produtos/{id}")
def buscar_produto(id: int):
    try:
        produto = estoque.buscar_produto(id)
        return produto

    except ValueError as erro:
        raise HTTPException(status_code=404, detail=str(erro))


@app.post("/produtos/{id}/entrada")
def entrada_estoque(id: int, dados: Quantidade):
    try:
        produto = estoque.entrada(id, dados.quantidade)
        return produto

    except ValueError as erro:
        raise HTTPException(status_code=400, detail=str(erro))


@app.post("/produtos/{id}/saida")
def saida_estoque(id: int, dados: Quantidade):
    try:
        produto = estoque.saida(id, dados.quantidade)
        return produto

    except ValueError as erro:
        raise HTTPException(status_code=400, detail=str(erro))