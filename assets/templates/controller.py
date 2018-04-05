from flask import Blueprint, abort

prefix = '/' + '<_name_>'

controller = Blueprint('<_name_>', __name__)

@controller.route('/')
def index():
    try:
        return "<_name_> Controller Index"
    except:
        abort(500)
