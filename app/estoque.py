from app.produtos import Produto


class Estoque:
    def __init__(self):
        self.produtos = []
        self.proximo_id = 1

    def cadastrar_produto(self, nome, preco, quantidade):
        if not nome:
            raise ValueError("O nome do produto não pode ficar vazio")

        if preco <= 0:
            raise ValueError("O preço deve ser maior que zero")

        if quantidade < 0:
            raise ValueError("A quantidade não pode ser negativa")

        produto = Produto(
            self.proximo_id,
            nome,
            preco,
            quantidade
        )

        self.produtos.append(produto)
        self.proximo_id += 1

        return produto

    def listar_produtos(self):
        return self.produtos

    def buscar_produto(self, id):
        for produto in self.produtos:
            if produto.id == id:
                return produto

        raise ValueError("Produto não encontrado")

    def entrada(self, id, quantidade):
        if quantidade <= 0:
            raise ValueError("A quantidade deve ser maior que zero")

        produto = self.buscar_produto(id)
        produto.estoque += quantidade

        return produto

    def saida(self, id, quantidade):
        if quantidade <= 0:
            raise ValueError("A quantidade deve ser maior que zero")

        produto = self.buscar_produto(id)

        if quantidade > produto.estoque:
            raise ValueError("Não há estoque suficiente")

        produto.estoque -= quantidade

        return produto