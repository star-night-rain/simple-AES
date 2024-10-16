from utils import *


def aes_decrypt(ciphertext):
    pass


def encrypt(plaintext, secret_key):
    ciphertext = None
    if is_binary_string(plaintext):
        ciphertext = aes_encrypt(plaintext, secret_key)
    else:
        pass
    print(ciphertext)
    return {'ciphertext': ciphertext}


def aes_encrypt(plaintext, secret_key):
    secret_keys = expand_secret_key(secret_key)
    mid_text = xor(plaintext, secret_keys[0])
    print(f'mid_text: {mid_text}')
    mid_text = encrypt_round_function(mid_text, secret_keys[1])
    print(f'mid_text: {mid_text}')
    mid_text = encrypt_round_function(mid_text, secret_keys[2], True)
    return mid_text
