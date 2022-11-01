from unittest import TestCase


from file_security_service import FileSecurityService


class TestFileSecurityService(TestCase):
    def setUp(self) -> None:
        self.service = FileSecurityService()


class TestMethodsMain(TestFileSecurityService):
    def test_get_list_of_files_empty(self):
        self.assertEqual(self.service.get_list_of_files(), [])

    def test_get_list_of_files(self):
        self.assertIsInstance(self.service.get_list_of_files(), list)

    def test_check_rsa_keys_none(self):
        self.assertEqual(self.service.check_rsa_keys(), -1)

    def test_check_rsa_keys(self):
        self.assertIsInstance(self.service.check_rsa_keys(), int)
