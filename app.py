from flask import Flask, jsonify
from stellar_sdk import Keypair

app = Flask(__name__)

@app.route("/")
def main():
    keypair = Keypair.random()
    resp = {
        'secret': keypair.secret,
        'public': keypair.public_key
    }
    return jsonify(resp)