from flask import render_template, request, redirect, url_for
from .domain.services import FuncionarioService, ContratacaoService

def register_routes(app):
    @app.route('/')
    def index():
        contratacoes = ContratacaoService.listar_contratacoes()
        funcionarios = FuncionarioService.listar_funcionarios()
        return render_template('index.html', contratacoes=contratacoes, funcionarios=funcionarios)

    @app.route('/cadastro', methods=['POST'])
    def cadastro():
        nome = request.form.get('nome')
        email = request.form.get('email')
        telefone = request.form.get('telefone')
        funcao = request.form.get('funcao')
        
        FuncionarioService.cadastrar_funcionario(nome, email, telefone, funcao)
        
        return redirect(url_for('index'))

    @app.route('/contratacao', methods=['POST'])
    def contratacao():
        servico = request.form.get('servico')
        data = request.form.get('data')
        detalhes = request.form.get('detalhes')
        funcionario_id = request.form.get('funcionario_id')
        
        ContratacaoService.contratar_servico(servico, data, detalhes, funcionario_id)
        
        return redirect(url_for('index'))

