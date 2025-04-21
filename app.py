# Importa a classe Flask do módulo flask
from flask import Flask

# Cria uma instância do aplicativo Flask
app = Flask(__name__)

# Define uma rota para a URL raiz ("/")
@app.route("/")
def hello_world():
    # Retorna uma resposta simples quando o usuário acessa a página inicial
    return("200")

# Define uma rota para a URL "/about"
@app.route("/about")
def sobre():
    # Retorna uma mensagem quando o usuário acessa a página "Sobre"
    return "Página Sobre Games"

# Verifica se o script está sendo executado localmente (e não importado como módulo)
if __name__ == "__main__":
    # Inicia o servidor em modo de depuração (debug=True)
    app.run(debug=True)
