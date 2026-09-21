from src.main import *
from unittest.mock import patch


def test_root():
    result = read_root()
    yield result
    assert result == {"Message": "Hello, World"}



def test_funcaoteste():
    with patch('random.randint', return_value=67):
        result = funcaoteste()
        yield result

    assert result == {"teste": True, "num aleatorio": 67}



def test_create_estudante(estudante: Estudante):
    estudante_teste = Estudante(name=" Eduardo", curso="medicina", ativo=False)
    result = create_estudante(estudante_teste)
    yield result
    assert estudante_teste == result



def test_update_estudante_negativo():
    result = update_estudante(-5)
    yield result
    assert not result

def test_update_estudante_positivo():
    result = update_estudante(5)
    yield result
    assert result


def test_delete_estudante_negativo():
    result =delete_estudante(-5)
    yield result
    assert not result

def test_delete_estudante_positivo():
    result = delete_estudante(5)
    yield result
    assert result

