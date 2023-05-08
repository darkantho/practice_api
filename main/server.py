from flask import Flask, jsonify, request
from products import products

app = Flask(__name__)

@app.route("/ping")
def ping():
    return jsonify({"message": "Pong!"})

@app.route("/products",methods=["GET"])
def getProducts():
    return jsonify({"products":products,"message":"Lista de productos"})

@app.route("/products",methods=["POST"])
def add_new_product():
    new_product = {
        "name": request.json["name"],
        "price": request.json["price"],
        "quantity": request.json["quantity"]
    }
    products.append(new_product)
    return jsonify({"message":"Producto Agregado","Products":products})

@app.route("/products/<string:product_name>")
def getProduct(product_name):
    product_found = [product for product in products if product["name"] == product_name]
    if len(product_found)>0:
        return jsonify({"product":product_found[0]})
    else:
        return jsonify({"message":"product not found"})

@app.route("/products/<string:product_name>",methods=["PUT"])
def updateProduct(product_name):
    product_found = [product for product in products if product["name"] == product_name]
    if len(product_found)>0:
        product_found[0]["name"] = request.json["name"]
        product_found[0]["price"] = request.json["price"]
        product_found[0]["quantity"] = request.json["quantity"]
        return jsonify({"message":"Product Update",
                        "product": product_found
                        })
    else:
        return jsonify({"message":"product not found"})

@app.route("/products/<string:product_name>",methods=["DELETE"])
def deleteProduct(product_name):
    product_found = [product for product in products if product["name"] == product_name]
    if len(product_found)>0:
        products.remove(product_found[0])
        return jsonify({"message":"product deleted",
                        "product":products})
    else:
        return jsonify({"message":"product not found"})

if __name__ == '__main__':
    app.run(debug=True, port=4000)

