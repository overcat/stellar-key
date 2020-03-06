from flask import Flask, jsonify, response
from stellar_sdk import Keypair

app = Flask(__name__)

def add_cors_headers(response):
    response.headers['Access-Control-Allow-Origin'] = '*'
    if request.method == 'OPTIONS':
        response.headers['Access-Control-Allow-Methods'] = 'DELETE, GET, POST, PUT'
        headers = request.headers.get('Access-Control-Request-Headers')
        if headers:
            response.headers['Access-Control-Allow-Headers'] = headers
    return response

app.after_request(add_cors_headers)

@app.route("/")
def main():
    keypair = Keypair.random()
    resp = {
        'secret': keypair.secret,
        'public': keypair.public_key
    }
    return jsonify(resp)
