from flask import Flask, request, jsonify

from AES import *

app = Flask(__name__)


# TODO 统一封装返回结果
# TODO 全局异常处理

@app.route('/')
def hello_world():  # put application's code here
    return 'Hello World!'


@app.post('/aes/encrypt/single/<data_type>')
def single_encrypt(data_type):
    data = request.get_json()
    plaintext = data['plaintext']
    secret_key = data['secretKey']

    result = None

    if data_type == 'bit':
        result = encrypt_bit(plaintext, secret_key)
    elif data_type == 'string':
        result = encrypt_string(plaintext, secret_key)

    return jsonify(result)


@app.post('/aes/encrypt/double')
def double_encrypt():
    data = request.get_json()
    plaintext = data['plaintext']
    secret_key = data['secretKey']

    result = double_aes_encrypt(plaintext, secret_key)

    return jsonify(result)


@app.post('/aes/encrypt/triple/<version>')
def triple_encrypt(version):
    data = request.get_json()
    plaintext = data['plaintext']
    secret_key = data['secretKey']

    result = None
    if version == 'v1':
        result = triple_aes_encrypt_v1(plaintext, secret_key)
    elif version == 'v2':
        result = triple_aes_encrypt_v2(plaintext, secret_key)

    return jsonify(result)


@app.post('/aes/decrypt/single/<data_type>')
def single_decrypt(data_type):
    data = request.get_json()
    ciphertext = data['ciphertext']
    secret_key = data['secretKey']

    result = None
    if data_type == 'bit':
        result = decrypt_bit(ciphertext, secret_key)
    elif data_type == 'string':
        result = decrypt_string(ciphertext, secret_key)

    return jsonify(result)


@app.post('/aes/decrypt/double')
def double_encrypt():
    data = request.get_json()
    ciphertext = data['ciphertext']
    secret_key = data['secretKey']

    result = double_aes_encrypt(ciphertext, secret_key)

    return jsonify(result)


@app.post('/aes/decrypt/triple/<version>')
def triple_encrypt(version):
    data = request.get_json()
    ciphertext = data['ciphertext']
    secret_key = data['secretKey']

    result = None
    if version == 'v1':
        result = triple_aes_decrypt_v1(ciphertext, secret_key)
    elif version == 'v2':
        result = triple_aes_decrypt_v2(ciphertext, secret_key)

    return jsonify(result)


@app.route('/aes/crack')
def crack():
    data = request.get_json()
    plaintexts = data['plaintexts']
    ciphertexts = data['ciphertexts']
    result = aes_crack(plaintexts, ciphertexts)
    return result


if __name__ == '__main__':
    app.run()
