from services.usuario_service import UsuarioService
from repositories.usuario_repository import UsuarioRepository
from config.database import Session
import os

def main():
    session=Session()
    repository=UsuarioRepository(session)
    service=UsuarioService(repository)

    while True:
        print("---|SENAI-2024|---")
        print("1 | Adicionar usuário")
        print("2 | Pesquisar usuário")
        print("3 | Atualizar usuário")
        print("4 | Excluir usuário")
        print("5 | Exibir todos os usuários")
        print("0 | Sair")
        opcao=input("Selecione a opção: ")
       
        match opcao:
            case "1":
                print("\nAdicionando usuário")
                nome=input("Informe seu nome: ")
                email=input("Informe seu email: ")
                senha=input("Informe sua senha: ")
                service.criar_usuario(nome=nome,email=email,senha=senha)
                
            case "2":
                try:
                    usuario_email = input("Digite o email do usuário que você deseja encontrar: ")

                    usuario = service.repository.pesquisar_usuario__por__email(usuario_email)

                    if usuario:
                        print(f"Usuário encontrado: ID: {usuario.id} | Nome: {usuario.nome} | Email: {usuario.email}")
                    else:
                        print("Usuário não encontrado.")

                except ValueError:
                    print("Insira um email válido.")
                except Exception as e:
                    print(f"Ocorreu um erro ao procurar o usuário: {e}")
                break

            case "3":
                print("Atualizando usuario")
                try:
                    usuario_id = int(input("Digite o ID do usuário a ser atualizado: "))

                    usuario = repository.buscar_por_id(usuario_id)
                    
                    if usuario:
                        print(f"Usuário encontrado: ID: {usuario.id} | Nome: {usuario.nome} | Email: {usuario.email}")

                        novoNome = input(f"Digite o novo nome (atual: {usuario.nome}): ")
                        novoEmail = input(f"Digite o novo email (atual: {usuario.email}): ")
                        novaSenha = input("Digite a nova senha: ")

                        service.atualizar_usuario(usuario_id, novoNome, novoEmail, novaSenha)
                        print("Usuário atualizado com sucesso!")
                    else:
                        print("Usuário não encontrado.")

                except ValueError:
                    print("Insira um ID válido.")
                except Exception as e:
                    print(f"Ocorreu um erro ao atualizar o usuário: {e}")
                break
              
                break

            case "4":
                print("Excluindo usuário")
                try:
                    usuario_id = int(input("Insira o ID do usuário a ser excluído: "))
                    usuario=service.repository.excluir_usuario(usuario_id)
                    print("Usuário excluido com sucesso")
                except ValueError:
                    print("Insira um ID válido.")
                   
            case "5":
                print("Exibir todos os usuários")

                service.listar_todos_usuarios()

                print("\nExibindo todos os usuários cadastrados:")

                usuarios = service.listar_todos_usuarios()

                if usuarios:
                    for usuario in usuarios:
                        print(f"ID: {usuario.id} | Nome: {usuario.nome} | Email: {usuario.email}")
                
                else:
                    print("Nenhum usuário cadastrado.")
                    break
               
            case "0":
                break

if __name__ == "__main__":
    os.system("cls||clear")
    main()