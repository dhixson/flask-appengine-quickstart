from flask import Flask, request
from types import ModuleType
import jwt
import json
import re
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
    return "Inventory and Products API"

@app.before_request
def before_request():
    """Default Middleware."""
    try:
        header = request.headers.get('Authorization')
        regex = r"(?:Bearer\s*)(\S+)\b"
        match = re.match(regex, header)
        data = jwt.decode(match.group(1), 'GgfkXtJ2ofNhwBv85WfbiEdFTFn5704A', algorithms=['HS256'])
        request.environ['X_CP_TENANT'] = data['tenant_id']
        request.environ['X_CP_ROLE'] = data['role']
    except:
        return "Unauthorized", 401

if __name__ == "__main__":
    # Only for debugging while developing
    app.run(host='0.0.0.0', debug=True, port=80)
