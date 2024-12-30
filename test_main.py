# test_main.py
import unittest
from main import reverse_string

class TestStringMethods(unittest.TestCase):

    def test_empty_string(self):
        self.assertEqual(reverse_string(""), "")

    def test_single_character(self):
        self.assertEqual(reverse_string("a"), "a")

    def test_palindrome(self):
        self.assertEqual(reverse_string("madam"), "madam")

    def test_regular_string(self):
        self.assertEqual(reverse_string("hello"), "olleh")

    def test_numeric_string(self):
        self.assertEqual(reverse_string("12345"), "54321")

    # Добавим заведомо неверный тест
    def test_failed_case(self):
        self.assertEqual(reverse_string("test"), "wrong_value")  # Этот тест не пройдет

if __name__ == '__main__':
    unittest.main()
