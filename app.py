from flask import Flask, jsonify, request

app = Flask(__name__)

from products import products

@app.route('/ping')
def ping():
    return jsonify({"message": "Pong!"})

@app.route('/v1/products')
def getProducts():
    return jsonify(products)

@app.route('/v1/products/<int:id_product>')
def getProduct(id_product):
    productsFound = [product for product in products if product['id'] == id_product]
    if (len(productsFound) > 0):
        return jsonify({"product": productsFound[0]})
    return jsonify({"message": "Product not found"})

@app.route('/v1/products', methods=['POST'])
def addProduct():
    new_product = {
        "id": 4,
        "name": request.json['name'],
        "price": request.json['price'],
        "quantity": request.json['quantity']
    }
    products.append(new_product)
    return jsonify({"message": "Product added successfully", "products": products})

@app.route('/v1/products/<int:id_product>', methods=['PUT'])
def editProduct(id_product):
    productsFound = [product for product in products if product['id'] == id_product]
    if (len(productsFound) > 0):
        productsFound[0]['name'] = request.json['name']
        productsFound[0]['price'] = request.json['price']
        productsFound[0]['quantity'] = request.json['quantity']
        return jsonify({"Message": "Product updated", "Product": productsFound[0]})
    return jsonify({"Message": "Product not found"})

@app.route('/v1/products/<int:id_product>', methods=['DELETE'])
def deleteProduct(id_product):
    productsFound = [product for product in products if product['id'] == id_product]
    if (len(productsFound)>0):
        print(products)
        print(productsFound)
        products.remove(productsFound[0])
        return jsonify({"Message": "Product deleted successfully", "Products": products})
    return jsonify({"Message": "Product not found"})

if __name__ == '__main__':
    app.run(debug=True, port=4000)

    