# Define a classe HttpUnprocessableEntityError que é uma subclasse de Exception
class HttpUnprocessableEntityError(Exception):

    # Define o método __init__ para inicializar uma instância da classe
    def __init__(self, message: str) -> None:
        # Chama o método __init__ da classe base (Exception) e passa a mensagem
        super().__init__(message)
        # Atribui a mensagem de erro à variável de instância 'message'
        self.message = message
        # Atribui um nome simbólico ao tipo de erro
        self.name = "UnprocessableEntity"
        # Define o código de status HTTP correspondente ao erro (422 - Unprocessable Entity)
        self.status_code = 422
