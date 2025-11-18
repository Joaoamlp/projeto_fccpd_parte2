import requests
from flask import Flask, jsonify, Response

app = Flask(__name__)

@app.route("/")
def pokemons_formatados():
    pokemons = requests.get("http://microservicoA:8000/pokemons").json()
    dados_formatados = "\n".join(
        f"{p['pokemon']} é do tipo {p['tipo']}" for p in pokemons
    )
    
    return Response(dados_formatados, mimetype="text/plain")

app.run(host="0.0.0.0", port=8000)
