from src.main import *
from unittest.mock import patch
import pytest


@pytest.mark.asyncio
async def test_root():
    result = await read_root()
    assert result == {"Message": "Hello, World"}


@pytest.mark.asyncio
async def test_funcaoteste():
    with patch('random.randint', return_value=67):
        result = await funcaoteste()

    assert result == {"teste": True, "num aleatorio": 67}


@pytest.mark.asyncio
async def test_create_estudante(estudante: Estudante):
    estudante_teste = Estudante(name=" Eduardo", curso="medicina", ativo=False)
    result = await create_estudante(estudante_teste)
    assert estudante_teste == result


@pytest.mark.asyncio
async def test_update_estudante_negativo():
    result = await update_estudante(-5)
    assert not result

@pytest.mark.asyncio
async def test_update_estudante_positivo():
    result = await update_estudante(5)
    assert result

@pytest.mark.asyncio
async def test_delete_estudante_negativo():
    result = await delete_estudante(-5)
    assert not result

@pytest.mark.asyncio
async def test_delete_estudante_positivo():
    result = await delete_estudante(5)
    assert result

