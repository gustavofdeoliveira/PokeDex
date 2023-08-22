import requests
from pymongo import MongoClient

# URL da API
api_url = "https://pokeapi.co/api/v2/pokemon"

# Obtém os dados da API
response = requests.get(api_url)
data = response.json()

# Conexão com o MongoDB
client = MongoClient('mongodb://localhost:27017/')
db = client['pokedex']
collection = db['pokemon']

# Extrai os resultados da resposta JSON
results = data['results']

# Armazena os resultados no MongoDB
for result in results:
    name = result['name']
    url = result['url']
    
    # Cria um documento para inserir no MongoDB
    pokemon_data = {
        'name': name,
        'url': url
    }
    
    # Insere o documento na coleção
    collection.insert_one(pokemon_data)
    
print("Dados inseridos no MongoDB.")
