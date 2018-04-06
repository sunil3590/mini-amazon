from flask import Flask, request, Response
import pymongo
from pymongo import MongoClient

client = MongoClient('localhost', 27017)
db = client.mini_amazon

app = Flask('mini-amazon')


@app.route('/health', methods=['GET'])
def health():
    return 'healthy\n'


@app.route('/', methods=['GET'])
def index():
    return "<h1>Welcome to Mini Amazon</h1>"


@app.route('/say-hello/<name>')
def say_hello(name):
    return '<h1>Hello, {0}!</h1>'.format(name)


@app.route('/products', methods=['POST'])
def products():
    product = dict()
    product['title'] = request.form['title']
    product['description'] = request.form['description']
    product['price'] = request.form['price']
    print(product)
    db.products_collection.insert_one(product)
    return Response('OK\n', 200)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
