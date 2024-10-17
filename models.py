class Result(object):
    def __init__(self, code, msg, data):
        self.code = code
        self.msg = msg
        self.data = data

    @classmethod
    def success(cls, data):
        return cls(0, 'success', data)

    @classmethod
    def error(cls, data):
        return cls(1, 'error', data)

    def to_dict(self):
        return {
            'code': self.code,
            'msg': self.msg,
            'data': self.data
        }


class AesEncryption(object):
    def __init__(self, ciphertext):
        self.ciphertext = ciphertext


class AesDecryption(object):
    def __init__(self, plaintext):
        self.plaintext = plaintext


class AesCrack(object):
    def __init__(self, count, secret_keys, duration):
        self.count = count
        self.secret_keys = secret_keys
        self.duration = duration
