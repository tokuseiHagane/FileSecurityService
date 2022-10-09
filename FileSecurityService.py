# Возможные импорты
import binascii
import base64, hashlib
from cryptography.fernet import Fernet


class FileSecurityService:
    encoded_password = b''

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
        if type(to_decode) is not bytes:
            return b''
        return b''

    def encode_fernet(self, to_encode: bytes) -> bytes:
        if type(to_encode) is not bytes:
            if type(to_encode) is None:
                return b''
            raise TypeError
        return b''

    def set_base64_key(self, password: str):
        try:
            key = hashlib.md5(password.encode('utf-8')).hexdigest()
            self.encoded_password = self.encode_base64(key.encode('utf-8'))
        except TypeError as te:
            print(f'got not str and error "{te}"')
            return -1
        except AttributeError as ae:
            print(f'got not str and error "{ae}"')
            return -1
        return 0

    def get_base64_key(self):
        return self.encoded_password

    def decode_3(self):
        pass

    def encode_3(self):
        pass

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
