from utils import *


def encrypt(plaintext, secret_key):
    if is_binary_string(plaintext):
        ciphertext = aes_encrypt(plaintext, secret_key)
    else:
        ciphertext = ''
    print(ciphertext)
    return {'ciphertext': ciphertext}


def decrypt(ciphertext, secret_key):
    if is_binary_string(ciphertext):
        plaintext = aes_decrypt(ciphertext, secret_key)
    else:
        plaintext = ''
    print(f'plaintext: {plaintext}')
    return {'plaintext': plaintext}


def aes_encrypt(plaintext, secret_key):
    secret_keys = expand_secret_key(secret_key)
    mid_text = xor(plaintext, secret_keys[0])
    print(f'mid_text: {mid_text}')
    mid_text = encrypt_round_function(mid_text, secret_keys[1])
    print(f'mid_text: {mid_text}')
    ciphertext = encrypt_round_function(mid_text, secret_keys[2], True)
    return ciphertext


def aes_decrypt(ciphertext, secret_key):
    secret_keys = expand_secret_key(secret_key)
    mid_text = xor(ciphertext, secret_keys[2])
    print(f'mid_text: {mid_text}')
    mid_text = decrypt_round_function(mid_text, secret_keys[1])
    print(f'mid_text: {mid_text}')
    plaintext = decrypt_round_function(mid_text, secret_keys[0], True)
    return plaintext
