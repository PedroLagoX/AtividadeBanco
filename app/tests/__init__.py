import pytest

from app.models.usuario_model import Usuario

def test_usuario_nome_vazio_mensagem_erro():
    with pytest.raises(ValueError,match="O nome está vazio"):
        Usuario("","pedrolago@gmail.com","pedro1212")

def test_usuario_nome_vazio_invalido_erro():
    with pytest.raises(TypeError,match="O nome está invalido"):
        Usuario(1,"pedrolago@gmail.com","pedro1212")

def test_usuario_email_vazio_mensagem_erro():
    with pytest.raises(ValueError,match="O email está vazio"):
        Usuario("Pedro Lago","","pedro1212")

def test_usuario_email_invalido_mensagem_erro():
    with pytest.raises(TypeError,match="O email está invalido"):
        Usuario("Pedro Lago",1,"pedro1212")

def test_usuario_senha_vazia_mensagem_erro():
    with pytest.raises(ValueError,match="A senha está vazia"):
        Usuario("Pedro Lago","pedrolago@gmail.com","")

def test_usuario_senha_invalida_mensagem_erro():
    with pytest.raises(TypeError,match="A senha está inválida"):
        Usuario("Pedro Lago","pedrolago@gmail.com",1)