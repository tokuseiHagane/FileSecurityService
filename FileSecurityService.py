"""Класс для шифрования/дешифрования файла.

с ключом или без с помощью RSA, Fernet, base64.

Raises:
    TypeError: не были переданны байты

Returns:
    None: Ничего не возвращает
"""
import base64
import binascii
import hashlib
from os import listdir
from os.path import isfile, join

import rsa
from cryptography.fernet import Fernet


class FileSecurityService:
    """Класс для шифрования/дешифрования файла.

    с ключом или без с помощью RSA, Fernet, base64.

    Raises:
        TypeError: не были переданны байты

    Returns:
        None: Ничего не возвращает
    """

    enc_password = b''
    public_key, private_key = None, None

    # Блок отвественности Кирилла
    def run(self) -> None:
        """Запуск основного приложения."""
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
                        self.get_file(file, 'base64', 'encryption')
                    pass
                elif option == 2:
                    for file in files_list:
                        self.get_file(file, 'base64', 'decoding')
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
                        self.get_file(file, 'rsa', 'decoding')
            elif choice == 3:
                print('\nВыберите операцию:\n'
                      'Кодировать - 1\n'
                      'Декодировать - 2\n')
                option = int(input("Операция: "))
                key = input('Пароль для fernet: ')
                if option == 1:
                    for file in files_list:
                        self.get_file(file, 'rsa', 'encryption', key)
                elif option == 2:
                    for file in files_list:
                        self.get_file(file, 'rsa', 'decoding', key)

    @staticmethod
    def get_list_of_files() -> list:
        """Получение списка файлов.

        Returns:
            list: Список файлов
        """
        directory = './files_to_work_with'
        return [f for f in listdir(directory) if isfile(join(directory, f))]

    @staticmethod
    def check_rsa_keys() -> int:
        """Проверка наличия файлов ключей.

        Returns:
            int: результат выполнения (0 - успешно, -1 - ошибка)
        """
        files = [f for f in listdir('./') if isfile(join('./', f))]
        if 'public.pem' in files and 'private.pem' in files:
            return 0
        else:
            return -1

    # Блок ответственности Константина
    @staticmethod
    def decode_base64(to_decode: bytes) -> bytes:
        """Докодировать из base64.

        Args:
            to_decode (bytes): байты для декодирования

        Returns:
            bytes: декодированные файлы
        """
        try:
            return base64.b64decode(to_decode)
        except binascii.Error as ascii_e:
            print(f'got wrong bytes and error "{ascii_e}"')
            return b''
        except TypeError as te:
            print(f'got non bytes and error "{te}"')
            return b''

    @staticmethod
    def encode_base64(to_encode: bytes) -> bytes:
        """Кодирование в base64.

        Args:
            to_encode (bytes): байты для кодировки в base64

        Returns:
            bytes: закодированные в base64 байты
        """
        return base64.b64encode(to_encode)

    def decode_fernet(self, to_decode: bytes) -> bytes:
        """Декодирование из Fernet.

        Args:
            to_decode (bytes): байты для декодировки

        Returns:
            bytes: декодированные байты
        """
        try:
            decoded = Fernet(self.enc_password).decrypt(to_decode)
        except TypeError as te:
            print(f'got not bytes and error "{te}"')
            return b''
        except ValueError as ve:
            print(f'got not bytes and error "{ve}"')
            return b''
        return decoded

    def encode_fernet(self, to_encode: bytes) -> bytes:
        """Кодирование в Fernet.

        Args:
            to_encode (bytes): байты для кодирования

        Returns:
            bytes: закодированные байты
        """
        try:
            cipher = Fernet(self.enc_password).encrypt(to_encode)
        except TypeError as te:
            print(f'got not bytes and error "{te}"')
            return b''
        except ValueError as ve:
            print(f'got not bytes and error "{ve}"')
            return b''
        return cipher

    def set_base64_key(self, password: str) -> int:
        """Установка base64 ключа.

        Args:
            password (str): Ключ для base64

        Returns:
            int: результат выполнения (0 - успешно, -1 - ошибка)
        """
        try:
            key = hashlib.md5(password.encode('utf-8')).hexdigest()
            self.enc_password = base64.urlsafe_b64encode(key.encode('utf-8'))
        except TypeError as te:
            print(f'got not str and error "{te}"')
            return -1
        except AttributeError as ae:
            print(f'got not str and error "{ae}"')
            return -1
        return 0

    def get_base64_key(self) -> bytes:
        """Экспорт ключа base64.

        Returns:
            bytes: ключ base64
        """
        return self.enc_password

    def decode_rsa(self, to_decode: bytes) -> bytes:
        """Декодирование через RSA.

        Args:
            to_decode (bytes): байты для декодировки

        Returns:
            bytes: декодированные байты
        """
        try:
            decoded = rsa.decrypt(to_decode, self.private_key)
        except rsa.pkcs1.DecryptionError as de:
            print(f'decryption failed with error {de}')
            return b''
        except TypeError as de:
            print(f'decryption failed with error {de}')
            return b''
        return decoded

    def encode_rsa(self, to_encode: bytes) -> bytes:
        """Кодирование RSA.

        Args:
            to_encode (bytes): байты для кодировки

        Raises:
            TypeError: не были переданы байты

        Returns:
            bytes: закодированные байты
        """
        try:
            if type(to_encode) is not bytes or to_encode == b'':
                raise TypeError
            encoded = rsa.encrypt(to_encode, self.public_key)
        except TypeError as te:
            print(f'encryption failed with error {te}')
            return b''
        return encoded

    def read_rsa_public_key(self, file_path: str) -> bytes:
        """Получение публичного ключа RSA.

        Args:
            file_path (str): путь до файла ключа

        Returns:
            bytes: полученный ключ
        """
        with open(file_path, mode='rb') as f:
            self.public_key = rsa.PublicKey.load_pkcs1(f.read())
        return self.public_key

    def read_rsa_private_key(self, file_path: str) -> bytes:
        """Получение приватного ключа RSA.

        Args:
            file_path (str): путь до файла ключа

        Returns:
            bytes: полученный ключ
        """
        with open(file_path, mode='rb') as f:
            self.private_key = rsa.PrivateKey.load_pkcs1(f.read())
        return self.private_key

    def make_rsa_public_private_key(self) -> list:
        """Создание публичного и приватного ключа RSA.

        Returns:
            list: список ключей [публичный, приватный]
        """
        self.public_key, self.private_key = rsa.newkeys(512)
        return [self.public_key, self.private_key]

    def save_rsa_public_key(self) -> int:
        """Сохранение публичного ключа в файл.

        Returns:
            int: результат выполнения (0 - успешно, -1 - ошибка)
        """
        try:
            with open('public.pem', mode='wb+') as f:
                f.write(self.public_key.save_pkcs1())
        except Exception as e:
            return -1
        return 0

    def save_rsa_private_key(self) -> int:
        """Сохранение приватного ключа в файл.

        Returns:
            int: результат выполнения (0 - успешно, -1 - ошибка)
        """
        try:
            with open('private.pem', mode='wb+') as f:
                f.write(self.private_key.save_pkcs1())
        except Exception as e:
            return -1
        return 0

    # Блок ответственности Михаила
    def get_file(self,
                 file_name: str,
                 action: str,
                 encryption: str,
                 key: bytes = None) -> bytes:
        """Получение данных из файла.

        Args:
            file_name (str): имя файла для обработки
            action (str): encode или decode (кодировать, декодировать)
            encryption (str): тип кодирования/декодирования
            key (bytes, optional): Ключ для base64. По умолчанию None.

        Returns:
            bytes: _description_
        """
        f = self.read_file(file_name)
        fil = None
        if action == 'encode':
            if encryption == 'rsa':
                self.read_rsa_public_key('./public.pem')
                self.read_rsa_private_key('./private.pem')
                fil = self.encode_rsa(f)
            if encryption == 'fernet':
                self.set_base64_key(key)
                fil = self.encode_fernet(f)
            if encryption == 'base64':
                fil = self.encode_base64(f)
                print(fil)
        elif action == 'decode':
            if encryption == 'rsa':
                self.read_rsa_public_key('./public.pem')
                self.read_rsa_private_key('./private.pem')
                fil = self.decode_rsa(f)
            if encryption == 'fernet':
                self.set_base64_key(key)
                fil = self.decode_fernet(f)
            if encryption == 'base64':
                fil = self.decode_base64(f)
        return fil

    @staticmethod
    def read_file(file_name: str) -> bytes:
        """Получение файла для кодирования/декодирования.

        Args:
            file_name (str): _имя файла

        Returns:
            bytes: данные из файла
        """
        path = f'files_to_work_with/{file_name}'
        with open(mode='r+b', file=path) as f:
            file_data = f.read()
        return file_data

    @staticmethod
    def write_file(data: bytes,
                   file_name: str,
                   action: str,
                   encryption: str) -> int:
        """Запись зашифрованного/расшифрованного файла.

        Args:
            data (bytes): данные для шифрования
            file_name (str): имя файла
            action (str): encode или decode (кодировать, декодировать)
            encryption (str): тип кодирования/декодирования

        Returns:
            int: результат выполнения (0 - успешно, -1 - ошибка)
        """
        try:
            if action == 'encode':
                path = f'files_to_work_with/{file_name}.{encryption}'
                with open(file=path, mode='w+b') as f:
                    f.write(data)
            elif action == 'decode':
                name = '.'.join(file_name.split('.')[:-1])
                path = f'files_to_work_with/{name}'
                with open(file=path, mode='w+b') as f:
                    f.write(data)
        except Exception as e:
            print(str(e))
            return -1
        return 0


if __name__ == '__main__':
    app = FileSecurityService()
    app.run()
