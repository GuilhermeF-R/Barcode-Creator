# Importa a aplicação Flask do módulo server.py localizado em src/main/server
from src.main.server.server import app

# Verifica se este script está sendo executado como o principal
if __name__ == "__main__":
    # Inicia a execução do servidor Flask
    # 'host='0.0.0.0'' especifica que o servidor estará disponível em todas as interfaces de rede
    # 'port=3000' especifica que o servidor estará ouvindo na porta 3000
#'debug=True' habilita o modo de depuração, o que facilita a detecção e
# resolução de problemas durante o desenvolvimento
    app.run(host='0.0.0.0', port=3000, debug=True)
    