import binascii
import os
from unittest import TestCase

import rsa

from file_security_service import FileSecurityService


class TestFileSecurityService(TestCase):
    def setUp(self) -> None:
        self.service = FileSecurityService()


# rsa
# base_64
# fernet
class TestMethodsEncodeDecode(TestFileSecurityService):
    rsa_public_global = None
    rsa_private_global = None
    # Base64
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

    # Fernet
    def test_fernet_encode_good(self):
        self.assertIsInstance(self.service.encode_fernet(b'some bytes to pass'), bytes)

    def test_fernet_encode_empty_bytes(self):
        self.assertEqual(first=self.service.encode_fernet(b''),
                         second=b'')

    def test_fernet_encode_not_bytes(self):
        for val in [-1, 0, 1, 234, 'some string', 12.43, True, False]:
            self.assertEqual(self.service.encode_fernet(val), b'')

    def test_fernet_encode_got_none(self):
        self.assertEqual(self.service.encode_fernet(None), b'')

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
        self.assertEqual(self.service.set_base64_key(2), -1)

    def test_get_base64_key(self):
        self.assertIsInstance(self.service.get_base64_key(), bytes)

    # RSA
    def test_make_rsa_public_private_key(self):
        self.assertEqual(self.service.make_rsa_public_private_key(),
                         [self.service.public_key, self.service.private_key])

    def test_save_rsa_public_key(self):
        self.service.make_rsa_public_private_key()
        self.assertEqual(self.service.save_rsa_public_key(), 0)

    def test_save_rsa_private_key(self):
        self.service.make_rsa_public_private_key()
        self.assertEqual(self.service.save_rsa_private_key(), 0)

    def test_read_rsa_public_key(self):
        self.assertIsInstance(self.service.read_rsa_public_key('./public.pem'), rsa.PublicKey)

    def test_read_rsa_private_key(self):
        self.assertIsInstance(self.service.read_rsa_private_key('./private.pem'), rsa.PrivateKey)

    def test_rsa_encode_good(self):
        self.service.make_rsa_public_private_key()
        self.assertIsInstance(self.service.encode_rsa(b'some bytes to pass'), bytes)

    def test_rsa_encode_empty_bytes(self):
        self.service.make_rsa_public_private_key()
        self.assertEqual(first=self.service.encode_rsa(b''),
                         second=b'')

    def test_rsa_encode_not_bytes(self):
        self.service.make_rsa_public_private_key()
        for val in [-1, 0, 1, 234, 'some string', 12.43, True, False]:
            self.assertEqual(self.service.encode_rsa(val), b'')

    def test_rsa_encode_got_none(self):
        self.service.make_rsa_public_private_key()
        self.assertEqual(self.service.encode_rsa(None), b'')

    def test_rsa_decode_good(self):
        self.service.make_rsa_public_private_key()
        self.assertIsInstance(self.service.decode_rsa(b'c29tZSBieXRlcyB0byBwYXNz'), bytes)

    def test_rsa_decode_empty_bytes(self):
        self.service.make_rsa_public_private_key()
        self.assertEqual(first=self.service.decode_rsa(b''),
                         second=b'')

    def test_rsa_decode_not_bytes(self):
        self.service.make_rsa_public_private_key()
        for val in [-1, 0, 1, 234, 12.43, True, False, 'some string']:
            self.assertEqual(self.service.decode_rsa(val), b'')

    def test_rsa_decode_got_none(self):
        self.service.make_rsa_public_private_key()
        self.assertEqual(self.service.decode_rsa(None), b'')
