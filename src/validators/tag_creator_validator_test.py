#Importa a classe HttpUnprocessableEntityError do módulo
# src.errors.error_types.http_unprocessable_entity
from src.errors.error_types.http_unprocessable_entity import HttpUnprocessableEntityError
# Importa a função tag_creator_validator do módulo tag_creator_validator
from .tag_creator_validator import tag_creator_validator

# Define uma classe MockRequest para simular um objeto de requisição
class MockRequest:
    def __init__(self, json) -> None:
        self.json = json

# Define um teste para a função tag_creator_validator
def test_tag_creator_validator():
    # Cria um objeto de requisição simulado com um corpo válido
    req = MockRequest(json={ "product_code": "12345" })
    # Chama a função tag_creator_validator com a requisição simulada
    tag_creator_validator(req)

# Define um teste para a função tag_creator_validator quando ocorre um erro de validação
def test_tag_creator_validator_with_error():
    # Cria um objeto de requisição simulado com um corpo inválido (um número em vez de uma string)
    req = MockRequest(json={ "product_code": 12345 })

    # Tenta chamar a função tag_creator_validator com a requisição simulada
    try:
        tag_creator_validator(req)
        # Se nenhuma exceção for lançada, o teste falha
        assert False
    # Captura a exceção HttpUnprocessableEntityError que deve ser lançada quando a validação falha
    except Exception as exception:
        # Verifica se a exceção capturada é uma instância de HttpUnprocessableEntityError
        assert isinstance(exception, HttpUnprocessableEntityError)
