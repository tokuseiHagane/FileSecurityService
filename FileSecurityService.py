# Возможные импорты
import base64
import binascii
from math import floor


class FileSecurityService:
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

    def decode_2(self):
        pass

    def encode_2(self):
        pass

    def decode_3(self):
        pass

    def encode_3(self):
        pass

    def decode_4(self):
        pass

    def encode_4(self):
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
