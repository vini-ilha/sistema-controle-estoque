from app.estoque import Estoque


def test_cadastrar_produto():
    estoque = Estoque()

    produto = estoque.cadastrar_produto("Mouse", 80, 10)

    assert produto.nome == "Mouse"
    assert produto.preco == 80
    assert produto.estoque == 10


def test_cadastrar_produto_sem_nome():
    estoque = Estoque()

    try:
        estoque.cadastrar_produto("", 80, 10)
        assert False
    except ValueError:
        assert True


def test_cadastrar_preco_negativo():
    estoque = Estoque()

    try:
        estoque.cadastrar_produto("Mouse", -10, 10)
        assert False
    except ValueError:
        assert True


def test_entrada_estoque():
    estoque = Estoque()
    produto = estoque.cadastrar_produto("Mouse", 80, 10)

    estoque.entrada(produto.id, 5)

    assert produto.estoque == 15


def test_saida_estoque():
    estoque = Estoque()
    produto = estoque.cadastrar_produto("Mouse", 80, 10)

    estoque.saida(produto.id, 3)

    assert produto.estoque == 7


def test_saida_maior_que_estoque():
    estoque = Estoque()
    produto = estoque.cadastrar_produto("Mouse", 80, 10)

    try:
        estoque.saida(produto.id, 15)
        assert False
    except ValueError:
        assert True


def test_produto_inexistente():
    estoque = Estoque()

    try:
        estoque.buscar_produto(999)
        assert False
    except ValueError:
        assert True


def test_quantidade_negativa():
    estoque = Estoque()

    try:
        estoque.cadastrar_produto("Mouse", 80, -1)
        assert False
    except ValueError:
        assert True