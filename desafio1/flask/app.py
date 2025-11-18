from flask import Flask
from datetime import datetime

app = Flask(__name__)

historico_requisicoes = []

@app.route('/')
def home():
    agora = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    historico_requisicoes.append(agora)

    resposta = "<h1>Servidor Flask rodando!</h1>"
    resposta += "<h2>Histórico de requisições:</h2><ul>"
    for r in historico_requisicoes:
        resposta += f"<li>{r}</li>"
    resposta += "</ul>"
    return resposta

@app.route('/healthcheck')
def healthcheck():
    return "OK", 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
