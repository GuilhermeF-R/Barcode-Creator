# Importa a classe HttpResponse do módulo src.views.http_types.http_response
from src.views.http_types.http_response import HttpResponse
# Importa a classe HttpUnprocessableEntityError do módulo .error_types.http_unprocessable_entity
from .error_types.http_unprocessable_entity import HttpUnprocessableEntityError

# Define a função handle_errors que trata exceções e retorna uma resposta HTTP
def handle_errors(error: Exception) -> HttpResponse:
    # Verifica se a exceção é uma instância de HttpUnprocessableEntityError
    if isinstance(error, HttpUnprocessableEntityError):
        # Se for, cria uma resposta HTTP com o código de status e a mensagem de erro adequados
        return HttpResponse(
            status_code=error.status_code,
            body={
                "errors": [{
                    "title": error.name,
                    "detail": error.message
                }]
            }
        )

#Se a exceção não for do tipo HttpUnprocessableEntityError, trata-a como um erro interno do servidor
    return HttpResponse(
        status_code=500,
        body={
            "errors": [{
                "title": "Server Error",
                "detail": str(error)
            }]
        }
    )
