import bisect

from utils import *
import time


def single_aes_encrypt(plaintext, secret_key):
    secret_keys = expand_secret_key(secret_key)
    mid_text = xor(plaintext, secret_keys[0])
    # print(f'mid_text: {mid_text}')
    mid_text = encrypt_round_function(mid_text, secret_keys[1])
    # print(f'mid_text: {mid_text}')
    ciphertext = encrypt_round_function(mid_text, secret_keys[2], True)
    return ciphertext


def single_aes_decrypt(ciphertext, secret_key):
    secret_keys = expand_secret_key(secret_key)
    mid_text = xor(ciphertext, secret_keys[2])
    # print(f'mid_text: {mid_text}')
    mid_text = decrypt_round_function(mid_text, secret_keys[1])
    # print(f'mid_text: {mid_text}')
    plaintext = decrypt_round_function(mid_text, secret_keys[0], True)
    return plaintext


def encrypt_bit(plaintext, secret_key):
    ciphertext = single_aes_encrypt(plaintext, secret_key)
    return {'ciphertext': ciphertext}


def encrypt_string(plaintext, secret_key):
    plaintext = preprocess(plaintext)
    ciphertext = ''
    for i in range(0, len(plaintext), 2):
        # print(plaintext[i])
        binary_string1 = char_to_binary(plaintext[i])
        binary_string2 = char_to_binary(plaintext[i + 1])
        # print(f'binary_string1: {binary_string1}')
        # print(f'binary_string2: {binary_string2}')
        mid_string = single_aes_encrypt(binary_string1 + binary_string2, secret_key)
        left = mid_string[0:8]
        right = mid_string[8:16]
        ciphertext += binary_to_char(left) + binary_to_char(right)

    return ciphertext
    # return {'ciphertext': ciphertext}


def decrypt_bit(ciphertext, secret_key):
    plaintext = single_aes_decrypt(ciphertext, secret_key)
    return {'plaintext': plaintext}


def decrypt_string(ciphertext, secret_key):
    ciphertext = preprocess(ciphertext)
    plaintext = ''
    for i in range(0, len(ciphertext), 2):
        binary_string1 = char_to_binary(ciphertext[i])
        binary_string2 = char_to_binary(ciphertext[i + 1])
        # print(f'binary_string1: {binary_string1}')
        # print(f'binary_string2: {binary_string2}')
        mid_string = single_aes_decrypt(binary_string1 + binary_string2, secret_key)
        left = mid_string[0:8]
        right = mid_string[8:16]
        plaintext += binary_to_char(left) + binary_to_char(right)
    return plaintext
    # return {'plaintext': plaintext}


def double_aes_encrypt(plaintext, secret_key):
    mid_text = encrypt_string(plaintext, secret_key[0:16])

    # print(f'mid_text: {mid_text}')
    ciphertext = encrypt_string(mid_text, secret_key[16:32])
    # print(f'ciphertext: {ciphertext}')
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


def binary_search(sorted_values, target):
    index = bisect.bisect_left(sorted_values, target)

    if index != len(sorted_values) and sorted_values[index] == target:
        return index
    else:
        return None


def crack(plaintexts, ciphertexts):
    start_time = time.time()

    keys = list()
    keys1, keys2 = crack_a_pair(plaintexts[0], ciphertexts[0])
    if len(plaintexts) == 1:
        for (key1, key2) in zip(keys1, keys2):
            keys.append(key1 + key2)
    else:
        for (key1, key2) in zip(keys1, keys2):
            flag = True
            for i in range(1, len(plaintexts)):
                if not check_secret_key(plaintexts[i], ciphertexts[i], key1, key2):
                    flag = False
                    break
            if flag:
                keys.append(key1 + key2)

    end_time = time.time()
    duration = f'{end_time - start_time:.3f}'
    print(f'duration:{duration}s')

    return keys


def check_secret_key(plaintext, ciphertext, key1, key2):
    mid_text1 = encrypt_string(plaintext, key1)
    mid_text2 = decrypt_string(ciphertext, key2)
    return mid_text1 == mid_text2


def crack_a_pair(plaintext, ciphertext):
    keys = list()
    generate_secret_keys(keys, '')

    keys1 = list()
    keys2 = list()

    mid_texts = list()
    for key in keys:
        mid_texts.append(encrypt_string(plaintext, key))
    indexed_mid_texts = list(enumerate(mid_texts))
    sorted_mid_texts = sorted(indexed_mid_texts, key=lambda x: x[1])
    sorted_values = [x[1] for x in sorted_mid_texts]

    cnt = 0
    for key in keys:
        mid_text = decrypt_string(ciphertext, key)
        index = binary_search(sorted_values, mid_text)
        cnt += 1
        if index is not None:
            original_index = sorted_mid_texts[index][0]
            keys1.append(keys[original_index])
            keys2.append(key)

    return keys1, keys2


def cbc_encrypt(plaintext, secret_key, initial_vector):
    plaintext = preprocess(plaintext)
    ciphertext = ''
    last_text = initial_vector
    for i in range(0, len(plaintext), 2):
        binary_string = char_to_binary(plaintext[i]) + char_to_binary(plaintext[i + 1])

        binary_string = xor(binary_string, last_text)

        mid_string = single_aes_encrypt(binary_string, secret_key)
        left = mid_string[0:8]
        right = mid_string[8:16]
        ciphertext += binary_to_char(left) + binary_to_char(right)
        last_text = mid_string
    return {'ciphertext': ciphertext}


def cbc_decrypt(ciphertext, secret_key, initial_vector):
    ciphertext = preprocess(ciphertext)
    plaintext = ''
    last_text = initial_vector
    for i in range(0, len(ciphertext), 2):
        binary_string = char_to_binary(ciphertext[i]) + char_to_binary(ciphertext[i + 1])
        mid_string = single_aes_decrypt(binary_string, secret_key)
        mid_string = xor(mid_string, last_text)
        left = mid_string[0:8]
        right = mid_string[8:16]
        plaintext += binary_to_char(left) + binary_to_char(right)
        last_text = binary_string
    return {'plaintext': plaintext}
