import unittest
from TextQRCodeGenerator import QRText
from WiFiQRCodeGenerator import QRWiFi
from LocationQRCodeGenerator import QRLocate
from ContactsQRCodeGenerator import QRContacts
from qr_reader import qr_reader


class TestQRText(unittest.TestCase):
    def test_qr_code_generation_text(self):
        self.assertRaises(ValueError, QRText.qr_code, "text", 10, "text", "text", "text", "text", "text", "text")
        self.assertEqual(QRText.qr_code("test", 7, 10, 12, "#FFFF", "#FFFF", True, "test"), 0)


class TestQRWiFi(unittest.TestCase):
    def test_qr_code_generation_wifi(self):
        self.assertRaises(ValueError, QRWiFi.qr_code, "test", "test", "test", "test", "text", "text", "text", 0)
        self.assertEqual(QRWiFi.qr_code("test", "test", "WPA", "text", 20, 7, "#FFF", "#000"), 0)


class TestQRLocate(unittest.TestCase):
    def test_qr_code_generation_location(self):
        self.assertRaises(ValueError, QRLocate.qr_code, "test", "test", "test", "test", "test", "test", "test")
        self.assertEqual(QRLocate.qr_code(0.0,0.0, 20, "test", 7, "#FFF", "#000"), "test")


class TestQrReader(unittest.TestCase):
    def test_qr_reader(self):
        self.assertEqual(qr_reader.image("test"), "test")
        self.assertRaises(Exception, qr_reader.image, 123)


class TestQRContaacts(unittest.TestCase):
    def test_qr_contacts(self):
        name = "test"
        email = "test@gmail.com"
        phone = "+380985805966"
        url = "http://test.com"
        scale = 20
        file_name = "test"

        self.assertEqual(QRContacts.qr_code("test",
                                            "test@gmail.com",
                                            "+380985805966",
                                            "http://test.com",
                                            20,
                                            "test",
                                            7,
                                            "#FFF",
                                            "#000"), 0)


if __name__ == '__main__':
    unittest.main()
