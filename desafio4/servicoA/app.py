from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/pokemons")
def pokemons():
    dados = [
                {
                    "pokemon": "Pikachu",
                    "tipo": "Elétrico"
                },
                {
                    "pokemon": "Charmander",
                    "tipo": "Fogo"
                },
                {
                    "pokemon": "Squirtle",
                    "tipo": "Água"
                },
                {
                    "pokemon": "Bulbasaur", 
                    "tipo": "Planta"
                },
                {
                    "pokemon": "Eevee",
                    "tipo": "Normal"
                },


            ]
    return jsonify(dados)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
