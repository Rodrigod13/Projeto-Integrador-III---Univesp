from app.domain.models.model import Funcionario
from app.infrastructure import db

class FuncionarioService:
    @staticmethod
    def cadastrar_funcionario(nome, email, telefone, funcao):
        novo_funcionario = Funcionario(nome=nome, email=email, telefone=telefone, funcao=funcao)
        db.session.add(novo_funcionario)
        db.session.commit()

    @staticmethod
    def listar_funcionarios():
        return Funcionario.query.all()

