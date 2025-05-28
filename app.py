from flask import Flask
from models.mensagem import db  
from controller.mensagem import mensagem_bp

app = Flask(__name__)

# Define a URL do banco de dados
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///mensagens.db'

# Inicializa o banco de dados com a aplicação Flask
db.init_app(app)

# Registra o Blueprint mensagem_bp na aplicação
app.register_blueprint(mensagem_bp)

mensagens=[
    { 
        "nome" :"roberta", "id": 1,"mensagem":"ola"     
    },
    
]



with app.app_context():
    db.create_all()



