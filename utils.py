import re

import constant


# determine whether a string is a 16-bit binary sequence
def is_binary_string(s):
    return bool(re.fullmatch(r'[01]{16}', s))


def xor(s1, s2):
    int_result = int(s1, 2) ^ int(s2, 2)
    str_result = bin(int_result)[2:]
    result = str_result.zfill(len(s1))
    return result


def x_n_fx(last_result):
    if last_result[0] == '0':
        result = last_result[1:] + '0'
    else:
        if last_result[3] == '1':
            result = '0' + last_result[2] + '01'
        else:
            result = '0' + last_result[2] + '11'
    return result


def multiply(x, y):
    z = '0000'
    xfx = x_n_fx(x)
    x2fx = x_n_fx(xfx)
    x3fx = x_n_fx(x2fx)
    if y[0] == '1':
        z = xor(z, x3fx)
    if y[1] == '1':
        z = xor(z, x2fx)
    if y[2] == '1':
        z = xor(z, xfx)
    if y[3] == '1':
        z = xor(z, x)
    return z


def g(text, round_constant, s_box):
    left = text[0:4]
    right = text[4:8]
    left = s_box[int(left[:2], 2), int(left[2:], 2)]
    right = s_box[int(right[:2], 2), int(right[2:], 2)]
    text = xor(right + left, round_constant)
    return text


def expand_secret_key(secret_key):
    secret_keys = list()
    secret_keys.append(secret_key)

    left = secret_key[0:8]
    right = secret_key[8:16]
    for i in range(2):
        new_left = xor(left, g(right, constant.ROUND_CONSTANT[i], constant.SUBSTITUTION_BOX))
        new_right = xor(new_left, right)
        secret_keys.append(new_left + new_right)
        left = new_left
        right = new_right
    return secret_keys


def mix_columns(mid_text, x, y):
    s00 = xor(multiply(x, mid_text[0:4]), multiply(y, mid_text[4:8]))
    s10 = xor(multiply(y, mid_text[0:4]), multiply(x, mid_text[4:8]))
    s01 = xor(multiply(x, mid_text[8:12]), multiply(y, mid_text[12:16]))
    s11 = xor(multiply(y, mid_text[8:12]), multiply(x, mid_text[12:16]))
    return s00 + s10 + s01 + s11


def encrypt_round_function(plaintext, secret_key, last=False):
    mid_text = ''
    for i in range(0, len(plaintext), 4):
        mid_text += constant.SUBSTITUTION_BOX[int(plaintext[i:i + 2], 2), int(plaintext[i + 2:i + 4], 2)]
    mid_text = mid_text[0:4] + mid_text[12:16] + mid_text[8:12] + mid_text[4:8]
    if not last:
        mid_text = mix_columns(mid_text, '0001', '0100')
    state = xor(mid_text, secret_key)
    return state


def decrypt_round_function(ciphertext, secret_key, last=False):
    ciphertext = ciphertext[0:4] + ciphertext[12:16] + ciphertext[8:12] + ciphertext[4:8]

    mid_text = ''

    for i in range(0, len(ciphertext), 4):
        mid_text += constant.INVERSE_SUBSTITUTION_BOX[int(ciphertext[i:i + 2], 2), int(ciphertext[i + 2:i + 4], 2)]

    mid_text = xor(mid_text, secret_key)

    state = mid_text
    if not last:
        state = mix_columns(mid_text, '1001', '0010')

    return state


def char_to_binary(char):
    ascii_code = ord(char)
    binary_string = format(ascii_code, '08b')
    return binary_string


def binary_to_char(binary_string):
    ascii_code = int(binary_string, 2)
    char = chr(ascii_code)
    return char


def preprocess(text):
    if len(text) % 2 == 1:
        text += ' '
    return text


def generate_secret_keys(secret_keys, current_key):
    if len(current_key) == 16:
        secret_keys.append(current_key)
        return
    generate_secret_keys(secret_keys, current_key + '0')
    generate_secret_keys(secret_keys, current_key + '1')
