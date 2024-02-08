# Importa a classe Flask do módulo flask
from flask import Flask
# Importa o blueprint tags_routes_bp do módulo src.main.routes.tag_routes
from src.main.routes.tag_routes import tags_routes_bp

# Cria uma instância da aplicação Flask
app = Flask(__name__)

# Registra o blueprint tags_routes_bp na aplicação
app.register_blueprint(tags_routes_bp)
