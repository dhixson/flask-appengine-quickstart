from flask import Blueprint, abort

prefix = '/' + 'Nodes'

controller = Blueprint('Nodes', __name__)

@controller.route('/')
def index():
    try:
        return "Nodes Controller Index"
    except:
        abort(500)
