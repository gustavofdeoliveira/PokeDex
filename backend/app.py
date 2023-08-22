from pymongo import MongoClient
from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/pokemon', methods=['GET'])
def get_pokemon():
    client = MongoClient('mongodb://localhost:27017/')
    db = client['pokedex']
    collection = db['pokemon']
    pokemon_list = list(collection.find())
    result = [{'name': pokemon['name'], 'image': pokemon['image'], 'height': pokemon['height'], 'weight': pokemon['weight']} for pokemon in pokemon_list]
    return jsonify(result)

if __name__ == '__main__':
    app.run(debug=True)