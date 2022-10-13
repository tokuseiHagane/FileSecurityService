# Возможные импорты
import binascii
import base64, hashlib
from cryptography.fernet import Fernet
import rsa
from os import listdir
from os.path import isfile, join


class FileSecurityService:
    encoded_password = b''
    public_key, private_key = None, None

    # Блок отвественности Кирилла
    def __init__(self):
        pass

    def run(self):
        while True:
            files_list = self.get_list_of_files()
            print('Файлы в директории: ' + ', '.join(files_list))
            print('\nВыберите действие:\nВыход - 0\n'
                  'base64 - 1\n'
                  'rsa - 2\n'
                  'fernet - 3\n')

            choice = int(input("Действие: "))

            if choice == 0:
                break
            elif choice == 1:
                print('\nВыберите операцию:\n'
                      'Кодировать - 1\n'
                      'Декодировать - 2\n')
                option = int(input("Операция: "))
                if option == 1:
                    for file in files_list:
                        self.get_files(file, 'base64', 'encryption')
                    pass #file_name: str, action: str, tipe_encryption: str, key=None
                elif option == 2:
                    for file in files_list:
                        self.get_files(file, 'base64', 'decoding')
            elif choice == 2:
                print('\nВыберите операцию:\n'
                      'Кодировать - 1\n'
                      'Декодировать - 2\n')
                option = int(input("Операция: "))
                if option == 1:
                    for file in files_list:
                        if self.check_rsa_keys() == -1:
                            self.make_rsa_public_private_key()
                            self.save_rsa_private_key()
                            self.save_rsa_public_key()
                        self.get_file(file, 'rsa', 'decoding')
                elif option == 2:
                    if self.check_rsa_keys() == -1:
                        self.make_rsa_public_private_key()
                        self.save_rsa_private_key()
                        self.save_rsa_public_key()
                    for file in files_list:
                        self.get_files(file, 'rsa', 'decoding')
            elif choice == 3:
                print('\nВыберите операцию:\n'
                      'Кодировать - 1\n'
                      'Декодировать - 2\n')
                option = int(input("Операция: "))
                key = input('Пароль для fernet: ')
                if option == 1:
                    self.get_files(file, 'rsa', 'encryption', key)
                elif option == 2:
                    self.get_files(file, 'rsa', 'decoding', key)

    def get_list_of_files(self):
        onlyfiles = [f for f in listdir('./files_to_work_with') if isfile(join('./files_to_work_with', f))]
        return onlyfiles

    def check_rsa_keys(self):
        files = [f for f in listdir('./') if isfile(join('./', f))]
        if 'public.pem' in files and 'private.pem' in files:
            return 0
        else:
            return -1

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
    def get_file(self, file_name: str, action: str, tipe_encryption: str, key=None):
        f = self.read_file(file_name)
        fil = None
        if action == 'encryption':
            if tipe_encryption == 'rsa':
                self.read_rsa_public_key('./public.pem')
                self.read_rsa_private_key('./private.pem')
                fil = self.encode_rsa(f)
            if tipe_encryption == 'fernet':
                self.set_base64_key(key)
                fil = self.encode_fernet(f)
            if tipe_encryption == 'base64':
                fil = self.encode_base64(f)
                print(fil)
        if action == 'decoding':
            if tipe_encryption == 'rsa':
                self.read_rsa_public_key('./public.pem')
                self.read_rsa_private_key('./private.pem')
                fil = self.decode_rsa(f)
            if tipe_encryption == 'fernet':
                self.set_base64_key(key)
                fil = self.decode_fernet(f)
            if tipe_encryption == 'base64':
                fil = self.decode_base64(f)
        return fil

    def read_file(self, file_name):
        file_data = None
        path = f'files_to_work_with/{file_name}'
        with open(mode='r+b', file=path) as f:
            file_data = f.read()
            return file_data

    def write_file(self, fil, file_name: str, action, tipe_encryption):
        file_date = None
        if action == 'encryption':
            path = f'files_to_work_with/{file_name}.{tipe_encryption}'
            file_date = open(mode='w+b', file=path)
            file_date.write(fil)
            file_date.close()
        if action == 'decoding':
            f = file_name.split('.')
            f = '.'.join(f[:-1])
            path = f'files_to_work_with/{f}'
            file_date = open(mode='w+b', file=path)
            file_date.write(fil)
            file_date.close()
        return str(file_date)


if __name__ == '__main__':
    app = FileSecurityService()
    app.run()

