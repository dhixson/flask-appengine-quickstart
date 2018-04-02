from flask import Blueprint, abort

<_name_>_controller = Blueprint('<_name_>', __name__)

@<_name_>_controller.route('/')
def index():
    try:
        return "<_name_> Controller Index"
    except:
        abort(500)
