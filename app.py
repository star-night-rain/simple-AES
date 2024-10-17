from flask import request, Flask
from flask_cors import CORS

import AES
from models import *
from result import flask_response

app = Flask(__name__)
CORS(app)


@app.post('/aes/encrypt/single/<data_type>')
def single_encrypt(data_type):
    data = request.get_json()
    print(data)
    plaintext = data['plaintext']
    secret_key = data['secretKey']
    ciphertext = None

    if data_type == 'bit':
        ciphertext = AES.encrypt_bit(plaintext, secret_key)
    elif data_type == 'string':
        ciphertext = AES.encrypt_string(plaintext, secret_key)

    result = AesEncryption(ciphertext)

    return flask_response(result)


@app.post('/aes/encrypt/double')
def double_encrypt():
    data = request.get_json()
    plaintext = data['plaintext']
    secret_key = data['secretKey']
    ciphertext = AES.double_aes_encrypt(plaintext, secret_key)

    result = AesEncryption(ciphertext)

    return flask_response(result)


@app.post('/aes/encrypt/triple/<version>')
def triple_encrypt(version):
    data = request.get_json()
    plaintext = data['plaintext']
    secret_key = data['secretKey']

    ciphertext = None
    if version == 'v1':
        ciphertext = AES.triple_aes_encrypt_v1(plaintext, secret_key)
    elif version == 'v2':
        ciphertext = AES.triple_aes_encrypt_v2(plaintext, secret_key)

    result = AesEncryption(ciphertext)
    return flask_response(result)


@app.post('/aes/decrypt/single/<data_type>')
def single_decrypt(data_type):
    data = request.get_json()
    ciphertext = data['ciphertext']
    secret_key = data['secretKey']

    plaintext = None
    if data_type == 'bit':
        plaintext = AES.decrypt_bit(ciphertext, secret_key)
    elif data_type == 'string':
        plaintext = AES.decrypt_string(ciphertext, secret_key)

    result = AesDecryption(plaintext)

    return flask_response(result)


@app.post('/aes/decrypt/double')
def double_decrypt():
    data = request.get_json()
    ciphertext = data['ciphertext']
    secret_key = data['secretKey']

    plaintext = AES.double_aes_decrypt(ciphertext, secret_key)
    result = AesDecryption(plaintext)
    return flask_response(result)


@app.post('/aes/decrypt/triple/<version>')
def triple_decrypt(version):
    data = request.get_json()
    ciphertext = data['ciphertext']
    secret_key = data['secretKey']

    plaintext = None
    if version == 'v1':
        plaintext = AES.triple_aes_decrypt_v1(ciphertext, secret_key)
    elif version == 'v2':
        plaintext = AES.triple_aes_decrypt_v2(ciphertext, secret_key)
    result = AesDecryption(plaintext)
    return flask_response(result)


@app.post('/aes/crack')
def crack():
    data = request.get_json()
    plaintexts = data['plaintexts']
    ciphertexts = data['ciphertexts']
    count, secret_keys, duration = AES.crack(plaintexts, ciphertexts)
    result = AesCrack(count, secret_keys, duration)
    return flask_response(result)


@app.post('/aes/cbc/encrypt')
def cbc_encrypt():
    data = request.get_json()
    plaintext = data['plaintext']
    secret_key = data['secretKey']
    initial_vector = data['initialVector']
    ciphertext = AES.cbc_encrypt(plaintext, secret_key, initial_vector)
    result = AesEncryption(ciphertext)
    return flask_response(result)


@app.post('/aes/cbc/decrypt')
def cbc_decrypt():
    data = request.get_json()
    ciphertext = data['ciphertext']
    secret_key = data['secretKey']
    initial_vector = data['initialVector']
    plaintext = AES.cbc_decrypt(ciphertext, secret_key, initial_vector)
    result = AesDecryption(plaintext)
    return flask_response(result)


@app.errorhandler(Exception)
def error_handler(error):
    return flask_response(str(error))


if __name__ == '__main__':
    app.run()
