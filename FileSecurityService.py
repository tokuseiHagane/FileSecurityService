# Возможные импорты
import binascii
import base64, hashlib
from cryptography.fernet import Fernet
import rsa


class FileSecurityService:
    encoded_password = b''
    public_key, private_key = None, None

    # Блок отвественности Кирилла
    def __init__(self):
        pass

    def run(self):
        pass

    def __gui_init(self):
        pass

    # Блок ответственности Константина
    def decode_base64(self, to_decode: bytes) -> bytes:
        try:
            return base64.b64decode(to_decode)
        except binascii.Error as ascii:
            print(f'got wrong bytes and error "{ascii}"')
            return b''
        except TypeError as te:
            print(f'got non bytes and error "{te}"')
            return b''

    def encode_base64(self, to_encode: bytes) -> bytes:
        return base64.b64encode(to_encode)

    def decode_fernet(self, to_decode: bytes) -> bytes:
        try:
            decoded = Fernet(self.encoded_password).decrypt(to_decode)
        except TypeError as te:
            print(f'got not bytes and error "{te}"')
            return b''
        except ValueError as ve:
            print(f'got not bytes and error "{ve}"')
            return b''
        return decoded

    def encode_fernet(self, to_encode: bytes) -> bytes:
        try:
            cipher = Fernet(self.encoded_password).encrypt(to_encode)
        except TypeError as te:
            print(f'got not bytes and error "{te}"')
            return b''
        except ValueError as ve:
            print(f'got not bytes and error "{ve}"')
            return b''
        return cipher

    def set_base64_key(self, password: str):
        try:
            key = hashlib.md5(password.encode('utf-8')).hexdigest()
            self.encoded_password = base64.urlsafe_b64encode(key.encode('utf-8'))
        except TypeError as te:
            print(f'got not str and error "{te}"')
            return -1
        except AttributeError as ae:
            print(f'got not str and error "{ae}"')
            return -1
        return 0

    def get_base64_key(self):
        return self.encoded_password

    def decode_rsa(self, to_decode: bytes):
        try:
            decoded = rsa.decrypt(to_decode, self.private_key)
        except rsa.pkcs1.DecryptionError as de:
            print(f'decryption failed with error {de}')
            return b''
        except TypeError as de:
            print(f'decryption failed with error {de}')
            return b''
        return decoded

    def encode_rsa(self, to_encode: bytes):
        try:
            if type(to_encode) is not bytes or to_encode == b'':
                raise TypeError
            encoded = rsa.encrypt(to_encode, self.public_key)
        except TypeError as te:
            print(f'encryption failed with error {te}')
            return b''
        return encoded

    def read_rsa_public_key(self, file_path: str):
        with open(file_path, mode='rb') as f:
            self.public_key = rsa.PublicKey.load_pkcs1(f.read())
        return self.public_key

    def read_rsa_private_key(self, file_path: str):
        with open(file_path, mode='rb') as f:
            self.private_key = rsa.PrivateKey.load_pkcs1(f.read())
        return self.private_key

    def make_rsa_public_private_key(self):
        self.public_key, self.private_key = rsa.newkeys(512)
        return [self.public_key, self.private_key]

    def save_rsa_public_key(self):
        with open('public.pem', mode='wb+') as f:
            f.write(self.public_key.save_pkcs1())
        return 0

    def save_rsa_private_key(self):
        with open('private.pem', mode='wb+') as f:
            f.write(self.private_key.save_pkcs1())
        return 0

    # Блок ответственности Михаила
    def __get_file(self):
        pass

    def __read_file(self):
        pass

    def __write_file(self):
        pass

    def __create_file(self):
        pass


if __name__ == '__main__':
    app = FileSecurityService()
    print(app.decode_base64(b'some bytes to pass'))
