from flask import Flask, jsonify, render_template, request


app = Flask(__name__)  # __name__ is the unique name of this file


@app.route('/')
def home():
    return render_template('index.html')


# Data blueprint
# ==============

stores = [
    {
        'name': 'A Blueprint Store',
        'items': [
            {
                'name': 'a blueprint item',
                'price': 15.99
            }
        ]
    }
]


# POST - used to received data (in a server point of view)
# GET - used to send data back only (in a server point of view)

# GET requests API
# ================

# GET /store
#     --> get data of all stores
@app.route('/store')
def get_stores():
    return jsonify({'stores': stores})
    # Seul un dictionnaire prut être converti en JSON

# GET /store/<string:name>
#     --> get data about a store
@app.route('/store/<string:name>')
def get_store(name):
    for store in stores:
        if store['name'] == name:
            return jsonify(store)

    return jsonify({'message': "Store not found"})

# GET /store/<string:name>/item
#     --> get data of all items in a specific store
@app.route('/store/<string:name>/item')
def get_items_in_store(name):
    for store in stores:
        if store['name'] == name:
            return jsonify({'items': store['items']})

    return jsonify({'message': "Store not found"})


# POST requests API
# =================

# POST /store data: {name:}
#     --> create a new store
@app.route('/store', methods=['POST'])
def create_store():
    request_data = request.get_json()
    new_store = {
        'name': request_data['name'],
        'items': []
    }
    stores.append(new_store)
    return jsonify(new_store)

# POST /store/<string:name>/item data: {name:, price:}
#     --> create an item in a specific store
@app.route('/store/<string:name>/item', methods=['POST'])
def create_item_in_store(name):
    request_data = request.get_json()

    for store in stores:
        if store['name'] == name:
            new_item = {
                'name': request_data['name'],
                'price': request_data['price']
            }
            store['items'].append(new_item)
            return jsonify(new_item)

    return jsonify({'message': "Store not found"})


app.run(port=5000)  # launch the app on port 5000 (default value)
