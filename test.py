import json
import unittest

from app import app


class TestCase(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_encryption(self):
        print('encrypt the string "1234"')
        data = {
            'plaintext': '1234',
            'secretKey': '1010011100111011'
        }
        response = self.app.post('/aes/encrypt/single/string', json=data)
        result = json.loads(response.data)
        result = json.dumps(result, indent=4)
        print(f'The encryption result is: {result}')

    def test_decryption(self):
        print('decrypt the string "H¹°Z"')
        data = {
            'ciphertext': 'H¹°Z',
            'secretKey': '1010011100111011'
        }
        response = self.app.post('/aes/decrypt/single/string', json=data)
        result = json.loads(response.data)
        result = json.dumps(result, indent=4)
        print(f'The decryption result is: {result}')


if __name__ == '__main__':
    unittest.main()
