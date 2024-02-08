# Importa as classes Flask, request e jsonify do módulo flask
# Importa as classes Code128 e ImageWriter do módulo barcode
from flask import Flask, request, jsonify
from barcode import Code128
from barcode.writer import ImageWriter

# Cria uma instância de Flask
app = Flask(__name__)

# Define uma rota '/create_tag' que aceita apenas requisições POST
@app.route('/create_tag', methods=["POST"])
def create_tag():
    # Obtém os dados JSON da requisição
    body = request.json
    # Obtém o código do produto do corpo da requisição
    product_code = body.get('product_code')

    # Cria um código de barras Code128 com o código do produto e o escreve como uma imagem
    tag = Code128(product_code, writer=ImageWriter())
    # Define o caminho para salvar o arquivo de imagem da tag
    path_from_tag = f'{tag}'
    # Salva a imagem da tag no caminho especificado
    tag.save(path_from_tag)

    # Retorna um JSON contendo o caminho do arquivo da tag criada
    return jsonify({ "tag path": path_from_tag })

# Verifica se este script está sendo executado como o principal
if __name__ == '__main__':
    # Inicia a execução do servidor Flask
    # 'host='0.0.0.0'' especifica que o servidor estará disponível em todas as interfaces de rede
    # 'port=3000' especifica que o servidor estará ouvindo na porta 3000
    app.run(host='0.0.0.0', port=3000)
