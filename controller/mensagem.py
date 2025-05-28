from flask import Blueprint, request, jsonify
from models.mensagem import Mensagem, db 

# Cria um Blueprint chamado mensagem_bp
mensagem_bp = Blueprint('mensagem', __name__)


@mensagem_bp.route('/mensagens', methods=['POST'])
def criar_mensagem():
    dados = request.get_json()  # Pega os dados enviados pelo cliente
    nova_mensagem = Mensagem(conteudo=dados['conteudo'])  # Cria nova instância
    db.session.add(nova_mensagem)  # Adiciona ao banco de dados
    db.session.commit()  # Salva a operação
    return jsonify(nova_mensagem), 201  # Retorna a nova mensagem criada

@mensagem_bp.route('/mensagens', methods=['GET'])
def listar_mensagens():
    mensagens = Mensagem.query.all()  # Busca todas as mensagens
    return jsonify([{'id': m.id, 'conteudo': m.conteudo} for m in mensagens])  # Retorna em JSON


@mensagem_bp.route('/mensagens/<int:id>', methods=['GET'])
def obter_mensagem(id):
    mensagem = Mensagem.query.get_or_404(id)  # Busca a mensagem pelo ID
    return jsonify({'id': mensagem.id, 'conteudo': mensagem.conteudo})  # Retorna a mensagem encontrada


@mensagem_bp.route('/mensagens/<int:id>', methods=['PUT'])
def atualizar_mensagem(id):
    mensagem = Mensagem.query.get_or_404(id)  # Busca a mensagem pelo ID
    dados = request.get_json()  # Pega o novo conteúdo
    mensagem.conteudo = dados['conteudo']  # Atualiza a mensagem
    db.session.commit()  # Salva a alteração
    return jsonify({'id': mensagem.id, 'conteudo': mensagem.conteudo})  # Retorna a mensagem atualizada

@mensagem_bp.route('/mensagens/<int:id>', methods=['DELETE'])
def deletar_mensagem(id):
    mensagem = Mensagem.query.get_or_404(id) 
    db.session.delete(mensagem) 
    db.session.commit() 
    return jsonify({'mensagem': 'Mensagem deletada com sucesso.'})  # Retorna mensagem de sucesso