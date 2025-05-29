from flask import Flask, jsonify, request
from models.mensagem import db  
from controller.mensagem import mensagem_bp
import random


app = Flask(__name__)

# Define a URL do banco de dados
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///mensagens.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Inicializa o banco de dados com a aplicação Flask
db.init_app(app)

# Registra o Blueprint mensagem_bp na aplicação
app.register_blueprint(mensagem_bp)



@app.route('/mensagem', methods=['GET','PUT','DELETE','POST'])
def mensagem():
    nome = request.args.get('nome', 'Mundo')
    mensagens = [
        f'Olá, {nome}!',
        f'Bem-vindo, {nome}!',
        f'Tudo certo, {nome}?',
        f'Como vai, {nome}?',
        f'Saudações, {nome}!'
    ]
    return jsonify({'mensagem': random.choice(mensagens)})

with app.app_context():
    db.create_all()

if __name__ == '__main__':
    app.run(debug=True)
