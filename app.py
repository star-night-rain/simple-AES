from flask import Flask, request, jsonify
from AES import *

app = Flask(__name__)


@app.route('/')
def hello_world():  # put application's code here
    return 'Hello World!'


@app.post('/AES/encode')
def encode():
    data = request.get_json()
    print(data)
    plaintext = data['plaintext']
    secret_key = data['secretKey']
    return jsonify(encrypt(plaintext, secret_key))


@app.post('/AES/decode')
def decode():
    return None


@app.route('/AES/crack')
def crack():
    return None


if __name__ == '__main__':
    app.run()
