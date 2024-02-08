# Importa a função patch do módulo unittest.mock
from unittest.mock import patch
# Importa a classe BarcodeHandler do módulo src.drivers.barcode_handler
from src.drivers.barcode_handler import BarcodeHandler
# Importa a classe TagCreatorController do módulo .tag_creator_controller
from .tag_creator_controller import TagCreatorController

# Define um teste para o método create da classe TagCreatorController
@patch.object(BarcodeHandler, 'create_barcode')
def test_create(mock_create_barcode):
    # Valor simulado retornado pelo método create_barcode simulado
    mock_value = "image_path"
    # Configura o retorno do método create_barcode simulado
    mock_create_barcode.return_value = mock_value
    # Cria uma instância da classe TagCreatorController
    tag_creator_controller = TagCreatorController()

    # Chama o método create da TagCreatorController com o valor simulado
    result = tag_creator_controller.create(mock_value)

    # Verifica se o resultado é um dicionário
    assert isinstance(result, dict)
    # Verifica se o dicionário resultante contém a chave "data"
    assert "data" in result
    # Verifica se a chave "type" está presente no dicionário dentro de "data"
    assert "type" in result["data"]
    # Verifica se a chave "count" está presente no dicionário dentro de "data"
    assert "count" in result["data"]
    # Verifica se a chave "path" está presente no dicionário dentro de "data"
    assert "path" in result["data"]

    # Verifica se o valor de "type" no dicionário dentro de "data" é "Tag Image"
    assert result["data"]["type"] == "Tag Image"
    # Verifica se o valor de "count" no dicionário dentro de "data" é 1
    assert result["data"]["count"] == 1
#Verifica se o valor de "path" no dicionário dentro de"data" é o valor simulado com a extensão".png"
    assert result["data"]["path"] == f'{mock_value}.png'
