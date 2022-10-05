import binascii
from unittest import TestCase

from FileSecurityService import FileSecurityService


class TestFileSecurityService(TestCase):
    def setUp(self) -> None:
        self.service = FileSecurityService()


# rsa
# base_64
# fernet
class TestMethodsEncodeDecode(TestFileSecurityService):
    def test_base64_encode_good(self):
        self.assertEqual(first=self.service.encode_base64(b'some bytes to pass'),
                         second=b'c29tZSBieXRlcyB0byBwYXNz')

    def test_base64_encode_empty_bytes(self):
        self.assertEqual(first=self.service.encode_base64(b''),
                         second=b'')

    def test_base64_encode_not_bytes(self):
        for val in [-1, 0, 1, 234, 'some string', 12.43, True, False]:
            with self.assertRaises(TypeError):
                self.service.encode_base64(val)

    def test_base64_encode_got_none(self):
        with self.assertRaises(TypeError):
            self.service.encode_base64(None)

    def test_base64_decode_good(self):
        self.assertEqual(first=self.service.decode_base64(b'c29tZSBieXRlcyB0byBwYXNz'),
                         second=b'some bytes to pass')

    def test_base64_decode_empty_bytes(self):
        self.assertEqual(first=self.service.encode_base64(b''),
                         second=b'')

    def test_base64_decode_not_bytes(self):
        for val in [-1, 0, 1, 234, 12.43, True, False]:
            with self.assertRaises(TypeError):
                self.service.decode_base64(val)
        with self.assertRaises(binascii.Error):
            self.service.decode_base64('some string')

    def test_base64_decode_not_base64_bytes(self):
        with self.assertRaises(binascii.Error):
            self.service.decode_base64(b'some bytes to pass')

    def test_base64_decode_got_none(self):
        with self.assertRaises(TypeError):
            self.service.decode_base64(None)
