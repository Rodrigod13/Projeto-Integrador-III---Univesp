from app.domain.models.model import Contratacao
from app.infrastructure import db
from datetime import datetime

class ContratacaoService:
    @staticmethod
    def contratar_servico(servico, data, detalhes, funcionario_id):
        nova_contratacao = Contratacao(servico=servico, data=datetime.strptime(data, '%Y-%m-%d'), detalhes=detalhes, funcionario_id=funcionario_id)
        db.session.add(nova_contratacao)
        db.session.commit()

    @staticmethod
    def listar_contratacoes():
        return Contratacao.query.all()