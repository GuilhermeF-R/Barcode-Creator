# Importa o tipo Dict do módulo typing
from typing import Dict

# Define a classe HttpResponse
class HttpResponse:

    # Define o método __init__ para inicializar uma instância de HttpResponse
    def __init__(self, status_code: int, body: Dict) -> None:
        # Atribui o código de status da resposta
        self.status_code = status_code
        # Atribui o corpo da resposta como um dicionário
        self.body = body
