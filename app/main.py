from flask import Flask, request
from types import ModuleType
import os
import src.controllers as controllers
# Declare Flask Application
app = Flask(__name__)
# Load Controllers and Routes
for mod in controllers.__dict__.values():
    if type(mod) == ModuleType:
        app.register_blueprint(mod.controller, url_prefix=mod.prefix)

# Declare Application Default Routes
@app.route('/')
def index():
    return "Flask Quickstart"

@app.before_request
def before_request():
    """Default Middleware."""
    try:
        #place global middleware here
        pass
    except:
        return "Unauthorized", 401

if __name__ == "__main__":
    # Only for debugging while developing
    app.run(host='0.0.0.0', debug=True, port=8080)
