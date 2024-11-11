from models.usuario_model import Usuario
from sqlalchemy.orm import Session

class UsuarioRepository:
    def __init__(self, session: Session):
        self.session = session

    def salvar_usuario(self, usuario: Usuario):
        self.session.add(usuario)
        self.session.commit()
        self.session.refresh(usuario)

    def pesquisar_usuario__por__email(self, email:str):
        return self.session.query(Usuario).filter_by(email = email).first()
    
    def excluir_usuario(self, usuario: Usuario):
        self.session.delete(usuario)
        self.session.commit()
        self.session.refresh(usuario)

    def buscar_por_id(self, usuario_id):
        return self.session.query(Usuario).filter(Usuario.id == usuario_id).first()
    
    def listar_usuario(self):
        return self.session.query(Usuario).all()