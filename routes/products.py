from flask import Blueprint, request, jsonify
from app import mongo

products_bp = Blueprint('products', __name__)

@products_bp.route('/', methods=['GET'])
def get_products():
    products = list(mongo.db.products.find())
    for product in products:
        product['_id'] = str(product['_id'])
    return jsonify(products), 200

@products_bp.route('/', methods=['POST'])
def add_product():
    data = request.get_json()
    product = {
        "name": data['name'],
        "description": data['description'],
        "price": data['price'],
        "stock": data['stock']
    }
    mongo.db.products.insert_one(product)
    return jsonify({'message': 'Product added successfully'}), 201
