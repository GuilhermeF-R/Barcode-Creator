# Importa a classe Blueprint, request e jsonify do módulo flask
from flask import Blueprint, request, jsonify
# Importa a classe HttpRequest do módulo src.views.http_types.http_request
from src.views.http_types.http_request import HttpRequest
# Importa a classe TagCreatorView do módulo src.views.tag_creator_view
from src.views.tag_creator_view import TagCreatorView
# Importa a função handle_errors do módulo src.errors.error_handler
from src.errors.error_handler import handle_errors
# Importa a função tag_creator_validator do módulo src.validators.tag_creator_validator
from src.validators.tag_creator_validator import tag_creator_validator

# Cria um Blueprint chamado 'tags_routes'
tags_routes_bp = Blueprint('tags_routes', __name__)

# Define uma rota '/create_tag' dentro do Blueprint 'tags_routes' que aceita apenas requisições POST
@tags_routes_bp.route('/create_tag', methods=["POST"])
def create_tags():
    response = None
    try:
        # Valida o corpo da requisição usando a função tag_creator_validator
        tag_creator_validator(request)
        # Cria uma instância da classe TagCreatorView
        tag_creator_view = TagCreatorView()

        # Cria uma instância da classe HttpRequest com o corpo da requisição
        http_request = HttpRequest(body=request.json)
        # Chama o método validate_and_create da instância de TagCreatorView para criar a tag
        response = tag_creator_view.validate_and_create(http_request)
    # Captura exceções e chama a função handle_errors para tratá-las
    except Exception as exception:
        response = handle_errors(exception)

    # Retorna a resposta JSON com o corpo e o código de status da resposta
    return jsonify(response.body), response.status_code
