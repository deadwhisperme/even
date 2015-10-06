import unittest
import lib
class LibTest(unittest.TestCase):
    def test_palindrome(self):
        self.assertEqual(lib.palindrome('1221'), True)
        self.assertEqual(lib.palindrome('32223'), True)
        self.assertEqual(lib.palindrome('арозаупаланалапуазора'), True)
        self.assertEqual(lib.palindrome('0'), True)
    def test_non_palindrome(self):
        self.assertEqual(lib.palindrome('12345'), False)
unittest.main(verbosity=2)
