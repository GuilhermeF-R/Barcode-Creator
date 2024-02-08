# Importa a classe Validator do módulo cerberus
from cerberus import Validator

# Define um dicionário 'body' com dados a serem validados
body = {
    "data": {
        "elemento1": 123.98,
        "elemento2": "olaMundo",
    }
}

# Cria uma instância de Validator com regras de validação
body_validator = Validator({
    "data": {
        "type": "dict",  # O valor do campo 'data' deve ser um dicionário
        "schema": {      # Define um esquema para validar o dicionário 'data'
            "elemento1": { "type": "float", "required": True, "empty": False }, 
        #'elemento1' deve ser um float e não pode estar vazio
            "elemento2": { "type": "string", "required": True, "empty": True }, 
        #'elemento2' deve ser uma string e pode estar vazio
            "elemento3": { "type": "string", "required": False, "empty": False }, 
        #'elemento3' é opcional, se presente, deve ser uma string e não pode estar vazio
        }
    }
})

# Valida o dicionário 'body' usando as regras definidas em 'body_validator'
response = body_validator.validate(body)

# Se a validação falhar, imprime os erros de validação
if response is False:
    print(body_validator.errors)
else:
    # Se a validação for bem-sucedida, imprime 'Body OK'
    print('Body OK')
