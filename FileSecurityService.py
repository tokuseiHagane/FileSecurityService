# Возможные импорты
import hashlib

class FileSecurityService:
    # Блок отвественности Кирилла
    def __init__(self):
        pass

    def run(self):
        pass

    def __gui_init(self):
        pass

    # Блок ответственности Константина
    def __decode_1(self):
        pass

    def __encode_1(self):
        pass

    def __decode_2(self):
        pass

    def __encode_2(self):
        pass

    def __decode_3(self):
        pass

    def __encode_3(self):
        pass

    def __decode_4(self):
        pass

    def __encode_4(self):
        pass

    # Блок ответственности Михаила
    def get_file(self, file_name: str):
        #print(self.read_file(file_name))
        #my_hash1 = hashlib.md5()
        #my_hash1.update(self.read_file(file_name))
        #print(str(my_hash1.hexdigest()))
        pass

    def read_file(self, file_name):
        file_data = None
        with open(mode='r+b', file=file_name) as f:
            file_data = f.read()
            return file_data
        pass

    def __write_file(self):
        pass

    def __create_file(self):
        pass


if __name__ == '__main__':
    app = FileSecurityService()
    app.get_file('kok.txt')
    #app.run()
