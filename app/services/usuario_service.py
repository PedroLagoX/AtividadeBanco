from models.usuario_model import Usuario
from repositories.usuario_repository import UsuarioRepository

class UsuarioService:
    
    def __init__(self,repository:UsuarioRepository):
        self.repository=repository
        
    def criar_usuario(self,nome:str,email:str,senha:str):
        try:
            usuario=Usuario(nome=nome,email=email,senha=senha)
            novo_usuario=self.repository.pesquisar_usuario__por__email(usuario.email)

            if novo_usuario:
                print("Usuário já cadastrado!!")
                return

            self.repository.salvar_usuario(usuario)
            print("Usuário cadastrado com sucesso!!")

        except TypeError as erro:
            print(f"Erro ao salvar o usuario: {erro}")

        except Exception as erro:
            print(f"Ocorreu um erro inesperado: {erro}")

    def pesquisar_usuario_por_id(self, usuario_id):
        return self.repository.buscar_por_id(usuario_id)

    def atualizar_usuario(self, usuario_id, nome, email, senha):
        usuario = self.repository.buscar_por_id(usuario_id)
        if usuario:
            usuario.nome = nome
            usuario.email = email
            usuario.senha = senha
            self.repository.salvar_usuario(usuario) 
        else:
            raise ValueError("Usuário não encontrado para atualização")

    def listar_todos_usuarios(self):
        return self.repository.listar_usuarios()