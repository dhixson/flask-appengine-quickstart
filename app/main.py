from flask import Flask
import json
# ==== Controller Imports ====
from app.controllers.Users_controller import Users_controller
from app.controllers.Products_controller import Products_controller as Products
from app.controllers.Items_controller import Items_controller as Items
from app.controllers.Inventories_controller import Inventories_controller as Inventories
# ==== End Controller Imports ====
app = Flask(__name__)
# ==== Controllers ====
app.register_blueprint(Users_controller, url_prefix='/users')
app.register_blueprint(Products, url_prefix='/products')
app.register_blueprint(Items, url_prefix='/items')
app.register_blueprint(Inventories, url_prefix='/inventories')
# ==== End Controllers ====


@app.route('/')
def index():
    return "index"

if __name__ == "__main__":
    # Only for debugging while developing
    app.run(host='0.0.0.0', debug=True, port=80)
