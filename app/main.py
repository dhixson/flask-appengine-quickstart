from flask import Flask
import json
app = Flask(__name__)
# ==== Controllers ====
# ==== End Controllers ====

@app.route('/')
def index():
    return "index"

if __name__ == "__main__":
    # Only for debugging while developing
    app.run(host='0.0.0.0', debug=True, port=80)
