from flask import Flask


app = Flask(__name__)  # __name__ is the unique name of this file


@app.route('/')  # the root URL of the application
def home():  # the view associated to this route
    return "Hello, world!"


app.run(port=5000)  # launch the app on port 5000 (default value)
