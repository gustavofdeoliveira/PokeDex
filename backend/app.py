from flask import Flask
from pymongo import MongoClient

app = Flask(__name__)

client = MongoClient('localhost', 27017)
db = client['mongodb']
collection = db['images']

@app.route('/upload_image', methods=['POST'])
def upload_image():
    name = request.form['name']
    image = request.files['image'].read()

    image_data = {'name': name, 'image': Binary(image)}
    collection.insert_one(image_data)

    return 'Image uploaded'

if __name__ == '__main__':
    app.run(debug=True)