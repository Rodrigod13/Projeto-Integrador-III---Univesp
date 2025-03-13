<h1 align="center">🎓 Projeto Integrador III - Univesp</h1>


Este é um projeto desenvolvido para a disciplina de Projeto Integrador III da Univesp. 
Ele utiliza o Flask, um framework leve para aplicações web em Python.

## 📌 Tecnologias Utilizadas

Python 🐍 - Linguagem principal do projeto.
Flask 🔥 - Framework para o desenvolvimento web.
HTML, CSS e JavaScript 🎨
Banco de Dados 🗄️ - Pode ser SQLite, MySQL ou PostgreSQL.

## 📂 Estrutura do Projeto

project/
│── app/              # Código principal do aplicativo
│── instance/         # Configurações e banco de dados local
│── main.py           # Arquivo principal para rodar o Flask
│── requirements.txt  # Lista de dependências do projeto
│── venv/             # Ambiente virtual Python (não incluso no repositório)

## Como Executar o Projeto

Criar e ativar o ambiente virtual
Isso garante que todas as dependências do projeto sejam instaladas sem interferir em outros projetos no seu computador.

python -m venv venv

Ativando o ambiente virtual:

No Windows:
venv\Scripts\activate

No Linux/macOS:
source venv/bin/activate

Instalar as dependências
pip install -r requirements.txt

Isso instala todas as bibliotecas necessárias para o projeto rodar corretamente.

Executar o projeto
python main.py

Se tudo estiver correto, a aplicação estará rodando em http://127.0.0.1:5000 🎉

## 📌 Dicas

✅ Antes de rodar o projeto, ative o ambiente virtual.
✅ Caso o Flask não esteja instalado, rode:
pip install flask

✅ Para rodar em produção, use um servidor WSGI como Gunicorn ou uWSGI.

📜 Licença
Este projeto está licenciado sob a MIT License - veja o arquivo LICENSE para mais detalhes.
