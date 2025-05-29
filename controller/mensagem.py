from flask import Blueprint, request, jsonify
from models.mensagem import Mensagem, db 

mensagem_bp = Blueprint('mensagem', __name__)

@mensagem_bp.route('/mensagens', methods=['POST'])
def criar_mensagem():
    dados = request.get_json()  
    nova_mensagem = Mensagem(conteudo=dados['conteudo']) 
    db.session.add(nova_mensagem)  
    db.session.commit() 
    return jsonify({'id': nova_mensagem.id, 'conteudo': nova_mensagem.conteudo}), 201  

@mensagem_bp.route('/mensagens', methods=['GET'])
def listar_mensagens():
    mensagens = Mensagem.query.all() 
    return jsonify([{'id': m.id, 'conteudo': m.conteudo} for m in mensagens])  

@mensagem_bp.route('/mensagens/<int:id>', methods=['GET'])
def obter_mensagem(id):
    mensagem = Mensagem.query.get_or_404(id) 
    return jsonify({'id': mensagem.id, 'conteudo': mensagem.conteudo}) 

@mensagem_bp.route('/mensagens/<int:id>', methods=['PUT'])
def atualizar_mensagem(id):
    mensagem = Mensagem.query.get_or_404(id)  
    dados = request.get_json() 
    mensagem.conteudo = dados['conteudo'] 
    db.session.commit() 
    return jsonify({'id': mensagem.id, 'conteudo': mensagem.conteudo})

@mensagem_bp.route('/mensagens/<int:id>', methods=['DELETE'])
def deletar_mensagem(id):
    mensagem = Mensagem.query.get_or_404(id) 
    db.session.delete(mensagem) 
    db.session.commit() 
    return jsonify({'mensagem': 'Mensagem deletada com sucesso.'})
