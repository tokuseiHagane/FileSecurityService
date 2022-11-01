import unittest
from file_security_service import FileSecurityService


class FileSecurityServiceTest(unittest.TestCase):
    def setUp(self):
        self.FileSecurityService = FileSecurityService()

    def test_get_file(self):
        self.assertEqual(self.FileSecurityService.get_file('kok.txt', 'encryption', 'ras', 'aklsndjasnkjd'), b'ZG9neQ==')

    def test_read_file(self):
        self.assertEqual(self.FileSecurityService.read_file('kok.txt'), b'helloy world')

    def test_write_file(self):
        self.assertEqual(self.FileSecurityService.write_file(b'helloy world', 'kok.txt.base64', 'encryption', 'base64'), "<_io.BufferedRandom name='files_to_work_with/kok.txt.base64'>")



if __name__ == '__main__':
    unittest.main()
