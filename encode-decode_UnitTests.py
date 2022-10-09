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
        for val in [-1, 0, 1, 234, 12.43, True, False, 'some string']:
            self.assertEqual(self.service.decode_base64(val), b'')

    def test_base64_decode_not_base64_bytes(self):
        self.assertEqual(self.service.decode_base64(b'some bytes to pass'), b'')

    def test_base64_decode_got_none(self):
        self.assertEqual(self.service.decode_base64(None), b'')

    def test_fernet_encode_good(self):
        self.assertIsInstance(self.service.encode_fernet(b'some bytes to pass'), bytes)

    def test_fernet_encode_empty_bytes(self):
        self.assertEqual(first=self.service.encode_fernet(b''),
                         second=b'')

    def test_fernet_encode_not_bytes(self):
        for val in [-1, 0, 1, 234, 'some string', 12.43, True, False]:
            with self.assertRaises(TypeError):
                self.service.encode_fernet(val)

    def test_fernet_encode_got_none(self):
        with self.assertRaises(TypeError):
            self.service.encode_fernet(None)

    def test_fernet_decode_good(self):
        self.assertIsInstance(self.service.decode_fernet(b'c29tZSBieXRlcyB0byBwYXNz'), bytes)

    def test_fernet_decode_empty_bytes(self):
        self.assertEqual(first=self.service.decode_fernet(b''),
                         second=b'')

    def test_fernet_decode_not_bytes(self):
        for val in [-1, 0, 1, 234, 12.43, True, False, 'some string']:
            self.assertEqual(self.service.decode_fernet(val), b'')

    def test_fernet_decode_got_none(self):
        self.assertEqual(self.service.decode_fernet(None), b'')

    def test_set_base64_key(self):
        self.assertEqual(self.service.set_base64_key('some password'), 0)

    def test_set_base64_key_not_str(self):
        with self.assertRaises(TypeError):
            self.service.set_base64_key(2)

    def test_get_base64_key(self):
        self.assertIsInstance(self.service.get_base64_key(), bytes)