# Importa as classes Code128 e ImageWriter do módulo barcode
from barcode import Code128
from barcode.writer import ImageWriter

# Define a classe BarcodeHandler
class BarcodeHandler:
    # Define o método create_barcode que cria e salva um código de barras para um produto
    def create_barcode(self, product_code: str) -> str:
#Cria um código de barras Code128 com o código do produto e o configura para ser salvo
        tag = Code128(product_code, writer=ImageWriter())
        # Gera o caminho onde o arquivo da imagem do código de barras será salvo
        path_from_tag = f'{tag}'
        # Salva a imagem do código de barras no caminho especificado
        tag.save(path_from_tag)

        # Retorna o caminho do arquivo da imagem do código de barras
        return path_from_tag
