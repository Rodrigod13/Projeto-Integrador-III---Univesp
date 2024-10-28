from app.infrastructure import db

class Funcionario(db.Model):
    __tablename__ = 'funcionarios'

    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), nullable=False, unique=True)
    telefone = db.Column(db.String(20), nullable=False)
    funcao = db.Column(db.String(50), nullable=False)

    def __repr__(self):
        return f'<Funcionario {self.nome}>'

class Contratacao(db.Model):
    __tablename__ = 'contratacoes'

    id = db.Column(db.Integer, primary_key=True)
    servico = db.Column(db.String(100), nullable=False)
    data = db.Column(db.Date, nullable=False)
    detalhes = db.Column(db.Text)
    funcionario_id = db.Column(db.Integer, db.ForeignKey('funcionarios.id'))
    funcionario = db.relationship('Funcionario', backref='contratacoes')

    def __repr__(self):
        return f'<Contratacao {self.servico} na data {self.data}>'
