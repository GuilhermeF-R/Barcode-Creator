# Importa a classe Validator do módulo cerberus
from cerberus import Validator
#Importa o erro HttpUnprocessableEntityError do
#módulo src.errors.error_types.http_unprocessable_entity
from src.errors.error_types.http_unprocessable_entity import HttpUnprocessableEntityError

# Define uma função chamada tag_creator_validator que valida o corpo da requisição
def tag_creator_validator(request: any) -> None:
    # Cria uma instância de Validator com as regras de validação para o corpo da requisição
    body_validator = Validator({
        "product_code": { "type": "string", "required": True, "empty": False }
    })

    # Valida o corpo da requisição usando as regras definidas
    response = body_validator.validate(request.json)

#Se a validação falhar, lança uma exceção HttpUnprocessableEntityError com os erros de validação
    if response is False:
        raise HttpUnprocessableEntityError(body_validator.errors)
