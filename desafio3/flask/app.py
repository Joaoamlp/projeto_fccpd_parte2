from flask import Flask, jsonify
import psycopg2
import redis
import os

app = Flask(__name__)

db_config = {
    "host": os.getenv("DB_HOST", "postgres_desafio3"),
    "port": os.getenv("DB_PORT", 5432),
    "user": os.getenv("DB_USER", "postgres"),
    "password": os.getenv("DB_PASSWORD", "123"),
    "dbname": os.getenv("DB_NAME", "pokedb"),
}

cache_host = os.getenv('CACHE_HOST', 'cache')
cache_port = os.getenv('CACHE_PORT', 6379)

@app.route('/')
def home():
    return jsonify({'msg': 'API Flask rodando com sucesso!'})

@app.route('/pokemons')
def listar_pokemons():
    conn = psycopg2.connect(**db_config)
    cur = conn.cursor()
    cur.execute("SELECT * FROM pokemons;")
    pessoas = cur.fetchall()
    cur.close()
    conn.close()
    return jsonify(pessoas)

@app.route('/cache')
def testar_cache():
    r = redis.Redis(host=cache_host, port=cache_port)
    r.set('teste', 'funcionando')
    valor = r.get('teste').decode()
    return jsonify({'cache': valor})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)
