from flask import Flask, request, jsonify

import AES

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
        result = AES.encrypt_bit(plaintext, secret_key)
    elif data_type == 'string':
        result = AES.encrypt_string(plaintext, secret_key)

    return jsonify(result)


@app.post('/aes/encrypt/double')
def double_encrypt():
    data = request.get_json()
    plaintext = data['plaintext']
    secret_key = data['secretKey']
    # print(data)
    result = AES.double_aes_encrypt(plaintext, secret_key)

    return jsonify(result)


@app.post('/aes/encrypt/triple/<version>')
def triple_encrypt(version):
    data = request.get_json()
    plaintext = data['plaintext']
    secret_key = data['secretKey']

    result = None
    if version == 'v1':
        result = AES.triple_aes_encrypt_v1(plaintext, secret_key)
    elif version == 'v2':
        result = AES.triple_aes_encrypt_v2(plaintext, secret_key)

    return jsonify(result)


@app.post('/aes/decrypt/single/<data_type>')
def single_decrypt(data_type):
    data = request.get_json()
    ciphertext = data['ciphertext']
    secret_key = data['secretKey']

    result = None
    if data_type == 'bit':
        result = AES.decrypt_bit(ciphertext, secret_key)
    elif data_type == 'string':
        result = AES.decrypt_string(ciphertext, secret_key)

    return jsonify(result)


@app.post('/aes/decrypt/double')
def double_decrypt():
    data = request.get_json()
    ciphertext = data['ciphertext']
    secret_key = data['secretKey']

    result = AES.double_aes_decrypt(ciphertext, secret_key)

    return jsonify(result)


@app.post('/aes/decrypt/triple/<version>')
def triple_decrypt(version):
    data = request.get_json()
    ciphertext = data['ciphertext']
    secret_key = data['secretKey']

    result = None
    if version == 'v1':
        result = AES.triple_aes_decrypt_v1(ciphertext, secret_key)
    elif version == 'v2':
        result = AES.triple_aes_decrypt_v2(ciphertext, secret_key)

    return jsonify(result)


@app.post('/aes/crack')
def crack():
    data = request.get_json()
    plaintexts = data['plaintexts']
    ciphertexts = data['ciphertexts']
    result = AES.crack(plaintexts, ciphertexts)
    return result


@app.post('/aes/cbc/encrypt')
def cbc_encrypt():
    data = request.get_json()
    plaintext = data['plaintext']
    secret_key = data['secretKey']
    initial_vector = data['initialVector']
    result = AES.cbc_encrypt(plaintext, secret_key, initial_vector)
    return result


@app.post('/aes/cbc/decrypt')
def cbc_decrypt():
    data = request.get_json()
    ciphertext = data['ciphertext']
    secret_key = data['secretKey']
    initial_vector = data['initialVector']
    result = AES.cbc_decrypt(ciphertext, secret_key, initial_vector)
    return result


if __name__ == '__main__':
    app.run()
