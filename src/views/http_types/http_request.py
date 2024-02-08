# Importa o tipo Dict do módulo typing
from typing import Dict

# Define a classe HttpRequest
class HttpRequest:
    # Define o método __init__ para inicializar uma instância de HttpRequest
    def __init__(
            self,
            header: Dict = None,
            body: Dict = None,
            query_params: Dict = None
        ) -> None:
        # Atribui os cabeçalhos da requisição, se fornecidos; caso contrário, define como None
        self.header = header
        # Atribui o corpo da requisição, se fornecido; caso contrário, define como None
        self.body = body
# Atribui os parâmetros da consulta da requisição, se fornecidos; caso contrário, define como None
        self.query_params = query_params
