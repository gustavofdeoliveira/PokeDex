from flask import Flask, jsonify
from pymongo import MongoClient

app = Flask(__name__)

@app.route('/pokemon', methods=['GET'])
def get_pokemon():
    # Conexão com o MongoDB
    client = MongoClient('mongodb://localhost:27017/')
    db = client['pokedex']
    collection = db['pokemon']

    # Consulta todos os documentos na coleção
    pokemon_list = list(collection.find())

    # Transforma o resultado em um formato JSON
    result = [{'name': pokemon['name'], 'url': pokemon['url']} for pokemon in pokemon_list]

    return jsonify(result)

if __name__ == '__main__':
    app.run(debug=True)
