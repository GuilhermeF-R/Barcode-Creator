# Importa as classes necessárias dos módulos correspondentes
from src.views.http_types.http_request import HttpRequest
from src.views.http_types.http_response import HttpResponse
from src.controllers.tag_creator_controller import TagCreatorController

# Define a classe TagCreatorView
class TagCreatorView:
    # Comentário de docstring explicando a responsabilidade da classe
    '''
       responsability for interacting with HTTP 
    '''

    # Define um método para validar e criar uma tag
    def validate_and_create(self, http_request: HttpRequest) -> HttpResponse:
        # Instancia o controlador responsável pela criação de tags
        tag_creator_controller = TagCreatorController()

        # Obtém o corpo da requisição HTTP
        body = http_request.body
        # Obtém o código do produto do corpo da requisição
        product_code = body["product_code"]

        # Lógica de negócio: chama o método de criação de tag do controlador
        formatted_response = tag_creator_controller.create(product_code)

        # Retorna uma resposta HTTP com o status 200 e o corpo formatado
        return HttpResponse(status_code=200, body=formatted_response)
