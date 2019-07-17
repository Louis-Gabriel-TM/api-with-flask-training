from flask import Flask, jsonify


app = Flask(__name__)  # __name__ is the unique name of this file


# POST - used to received data (in a server point of view)
# GET - used to send data back only (in a server point of view)

# data blueprint
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

# POST /store data: {name:} --> create a new store
@app.route('/store', methods=['POST'])
def create_store():
    pass

# POST /store/<string:name>/item data: {name:, price:}
#     --> create an item in a specific store
@app.route('/store/<string:name>/item', methods=['POST'])
def create_item_in_store(name):
    pass

# GET /store/<string:name> --> get data about a store
@app.route('/store/<string:name>')
def get_store(name):
    pass

# GET /store --> get data of all stores
@app.route('/store')
def get_stores():
    return jsonify({'stores': stores})
    # Seul un dictionnaire prut être convertir en JSON

# GET /store/<string:name>/item --> get data of all items in a specific store
@app.route('/store/<string:name>/item')
def get_items_in_store(name):
    pass


app.run(port=5000)  # launch the app on port 5000 (default value)
