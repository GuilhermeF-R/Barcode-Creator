# Importa o tipo Dict do módulo typing
from typing import Dict
# Importa a classe BarcodeHandler do módulo src.drivers.barcode_handler
from src.drivers.barcode_handler import BarcodeHandler

# Define a classe TagCreatorController
class TagCreatorController:
    '''
        responsability for implementing business rules
    '''

    # Define o método create para criar uma tag com base no código do produto
    def create(self, product_code: str) -> Dict:
        # Chama métodos privados para criar a tag e formatar a resposta
        path_from_tag = self.__create_tag(product_code)
        formatted_response = self.__format_response(path_from_tag)
        # Retorna a resposta formatada
        return formatted_response

    # Método privado para criar a tag usando o BarcodeHandler
    def __create_tag(self, product_code: str) -> str:
        # Cria uma instância de BarcodeHandler
        barcode_handler = BarcodeHandler()
        # Chama o método create_barcode para criar a tag e obter o caminho da imagem
        path_from_tag = barcode_handler.create_barcode(product_code)
        return path_from_tag

    # Método privado para formatar a resposta
    def __format_response(self, path_from_tag: str) -> Dict:
        # Formata a resposta com informações sobre a tag criada
        return {
            "data": {
                "type": "Tag Image",
                "count": 1,
                "path": f'{path_from_tag}.png'
            }
        }
