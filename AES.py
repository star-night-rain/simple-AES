from utils import *
import time


def single_aes_encrypt(plaintext, secret_key):
    secret_keys = expand_secret_key(secret_key)
    mid_text = xor(plaintext, secret_keys[0])
    print(f'mid_text: {mid_text}')
    mid_text = encrypt_round_function(mid_text, secret_keys[1])
    print(f'mid_text: {mid_text}')
    ciphertext = encrypt_round_function(mid_text, secret_keys[2], True)
    return ciphertext


def single_aes_decrypt(ciphertext, secret_key):
    secret_keys = expand_secret_key(secret_key)
    mid_text = xor(ciphertext, secret_keys[2])
    print(f'mid_text: {mid_text}')
    mid_text = decrypt_round_function(mid_text, secret_keys[1])
    print(f'mid_text: {mid_text}')
    plaintext = decrypt_round_function(mid_text, secret_keys[0], True)
    return plaintext


def encrypt_bit(plaintext, secret_key):
    ciphertext = single_aes_encrypt(plaintext, secret_key)
    return {'ciphertext': ciphertext}


def encrypt_string(plaintext, secret_key):
    plaintext = preprocess(plaintext)
    ciphertext = ''
    for i in range(0, len(plaintext), 2):
        print(plaintext[i])
        binary_string1 = char_to_binary(plaintext[i])
        binary_string2 = char_to_binary(plaintext[i + 1])
        print(f'binary_string1: {binary_string1}')
        print(f'binary_string2: {binary_string2}')
        mid_string = single_aes_encrypt(binary_string1 + binary_string2, secret_key)
        left = mid_string[0:8]
        right = mid_string[8:16]
        ciphertext += binary_to_char(left) + binary_to_char(right)
    return {'ciphertext': ciphertext}


def decrypt_bit(ciphertext, secret_key):
    plaintext = single_aes_decrypt(ciphertext, secret_key)
    return {'plaintext': plaintext}


def decrypt_string(ciphertext, secret_key):
    ciphertext = preprocess(ciphertext)
    plaintext = ''
    for i in range(0, len(ciphertext), 2):
        binary_string1 = char_to_binary(ciphertext[i])
        binary_string2 = char_to_binary(ciphertext[i + 1])
        print(f'binary_string1: {binary_string1}')
        print(f'binary_string2: {binary_string2}')
        mid_string = single_aes_decrypt(binary_string1 + binary_string2, secret_key)
        left = mid_string[0:8]
        right = mid_string[8:16]
        plaintext += binary_to_char(left) + binary_to_char(right)
    return {'plaintext': plaintext}


def double_aes_encrypt(plaintext, secret_key):
    mid_text = encrypt_string(plaintext, secret_key[0:16])
    ciphertext = encrypt_string(mid_text, secret_key[16:32])
    return {'ciphertext': ciphertext}


def double_aes_decrypt(ciphertext, secret_key):
    mid_text = decrypt_string(ciphertext, secret_key[16:32])
    plaintext = decrypt_string(mid_text, secret_key[0:16])
    return {'plaintext': plaintext}


def triple_aes_encrypt_v1(plaintext, secret_key):
    mid_text = encrypt_string(plaintext, secret_key[0:16])
    mid_text = encrypt_string(mid_text, secret_key[16:32])
    ciphertext = encrypt_string(mid_text, secret_key[0:16])
    return {'ciphertext': ciphertext}


def triple_aes_encrypt_v2(plaintext, secret_key):
    mid_text = encrypt_string(plaintext, secret_key[0:16])
    mid_text = encrypt_string(mid_text, secret_key[16:32])
    ciphertext = encrypt_string(mid_text, secret_key[32:48])
    return {'ciphertext': ciphertext}


def triple_aes_decrypt_v1(ciphertext, secret_key):
    mid_text = decrypt_string(ciphertext, secret_key[0:16])
    mid_text = decrypt_string(mid_text, secret_key[16:32])
    plaintext = decrypt_string(mid_text, secret_key[0:16])
    return {'plaintext': plaintext}


def triple_aes_decrypt_v2(ciphertext, secret_key):
    mid_text = decrypt_string(ciphertext, secret_key[32:48])
    mid_text = decrypt_string(mid_text, secret_key[16:32])
    plaintext = decrypt_string(mid_text, secret_key[0:16])
    return {'plaintext': plaintext}


def aes_crack(plaintexts, ciphertexts):
    keys1 = []
    generate_secret_keys(keys1, '')
    keys2 = keys1

    secret_keys = list()

    start_time = time.time()
    for key1 in keys1:
        for key2 in keys2:
            is_same = True
            for i in range(0, len(plaintexts)):
                plaintext = plaintexts[i]
                ciphertext = ciphertexts[i]
                mid_text1 = decrypt_string(plaintexts, key1)
                mid_text2 = encrypt_string(ciphertexts, key2)
                if mid_text1 != mid_text2:
                    is_same = False
                    break
            if is_same == True:
                secret_keys.append(key1 + key2)
    end_time = time.time()
    duration = f'{end_time - start_time:.3f}'

    return {
        'sum': len(secret_keys),
        'secret_keys': secret_keys,
        'duration': duration
    }
