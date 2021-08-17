import unittest

from translator import english_to_french, french_to_english

class TestF2E(unittest.TestCase):
    def test_is_not_null(self):
        self.assertNotEqual(french_to_english("Bonjour"), "")
    def test_translation(self):
        self.assertEqual(french_to_english("Bonjour"), "Hello")

class TestE2F(unittest.TestCase):
    def test_is_not_null(self):
        self.assertNotEqual(english_to_french("Hello"), "")
    def test_translation(self):
        self.assertEqual(english_to_french("Hello"), "Bonjour")

unittest.main()