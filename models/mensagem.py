from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Mensagem(db.Model):
    __tablename__ = 'mensagens' 

    id = db.Column(db.Integer, primary_key=True) 
    conteudo = db.Column(db.String, nullable=False) 

    def __repr__(self):
        return f'<Mensagem {self.id}: {self.conteudo}>'
