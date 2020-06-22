from flask import Flask, jsonify, request, make_response, render_template

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/customers')
def customers():
    if request.authorization and request.authorization.username == 'adminuser' and request.authorization.password == 'adminpassword':
        response = {
            "customers": [
                {
                    "username": "customer1",
                    "email": "customer1@inshur.com",
                },
                {
                    "username": "customer2",
                    "email": "customer2@inshur.com",
                },
                {
                    "username": "customer3",
                    "email": "customer3@inshur.com",
                },
                {
                    "username": "customer4",
                    "email": "customer4@inshur.com",
                },
                {
                    "username": "customer5",
                    "email": "customer5@inshur.com",
                },
                {
                    "username": "customer6",
                    "email": "customer6@inshur.com",
                }
            ]
        }
        return response
    return make_response('Could not verify!', 401, {'www-Authenticate': 'Basic realm="Login Required"'})


@app.route('/product/<string:product_id>', methods=['GET'])
def product_api(product_id: str):
    if product_id == '1234':
        response = jsonify(
            productId=product_id,
            productName='Taxi',
            productVersion=1.0), 200
    else:
        response = jsonify(
            errorMessage=f'product {product_id} not found'), 404
    return response


@app.route('/products', methods=['GET'])
def products_api():
    response = {
        "products": [
            {
                "productId": "1234",
                "productName": "Taxi Product",
                "productVersion": 1.0
            },
            {
                "productId": "12345",
                "productName": "Courier Product",
                "productVersion": 1.0
            }
        ]
    }
    return response


if __name__ == '__main__':
    app.run()
