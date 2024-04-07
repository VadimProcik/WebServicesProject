from flask import Flask, jsonify, request
from pymongo import MongoClient
from bson.json_util import dumps, ObjectId
import secrets

app = Flask(__name__)

# Connect to MongoDB
client = MongoClient("mongodb://root:example@localhost:27017/")
db = client.Project
collection = db.getProducts

# Generate a random API key
API_KEY = secrets.token_hex(16) 
print("Generated API key:", API_KEY)

@app.route('/')
def root():
    api_urls = [
        {
            "url": "/getProducts",
            "description": "Fetch a list of products from the mongoDB database."
        },
        {
            "url": "/getTitles",
            "description": "Communicate with the Flask server to fetch the product data, while the server extracts the titles ."
        },
        {
            "url": "/insertProduct",
            "description": "Insert a new product into the database using Postman HTTP POST feature but only if you have the api key or else it will flag as an error."
        }
    ]

    return jsonify(api_urls)

@app.route('/getProducts', methods=['GET'])
def get_products():
    if request.method == 'GET':
        # Retrieve products from MongoDB
        products_data = list(collection.find())

        # Convert ObjectId to string for each product
        for product in products_data:
            product['_id'] = str(product['_id'])

        # Convert products data to JSON format
        products_json = dumps(products_data)

        # Return JSON response
        return products_json

@app.route('/getTitles', methods=['GET'])
def get_titles():
    if request.method == 'GET':
        # Retrieve product titles from MongoDB
        product_titles = [product['title'] for product in collection.find()]

        # Convert titles data to JSON format
        titles_json = dumps(product_titles)

        # Return JSON response
        return titles_json

@app.route('/insertProduct', methods=['POST'])
def insert_product():
    # Check if API key is provided in the request URL
    api_key = request.args.get('api_key')
    if api_key != API_KEY:
        return jsonify({'error': 'Invalid API key'}), 401

    # Extract product details from the request body
    product_id = request.json.get('id')
    product_title = request.json.get('title')
    product_cost = request.json.get('cost')

    # Validate input data
    if not all([product_id, product_title, product_cost]):
        return jsonify({'error': 'Missing product details'}), 400

    # Insert the product into the database
    new_product = {
        'id': product_id,
        'title': product_title,
        'cost': product_cost
    }
    result = collection.insert_one(new_product)

    # Return success message
    return jsonify({'message': 'Product inserted successfully', 'product_id': str(result.inserted_id)}), 201

if __name__ == '__main__':
    app.run(debug=True)