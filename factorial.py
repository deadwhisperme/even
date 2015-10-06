import unittest
import lib
class LibTest(unittest.TestCase):
    def test_factorial_non_negative_arg(self):
        self.assertEqual(lib.factorial(3), 6)
        self.assertEqual(lib.factorial(1), 1)
        self.assertEqual(lib.factorial(0), 0)
    def test_factorial_negative(self):
        self.assertEqual(lib.factorial(-1), 0)
unittest.main(verbosity=2)
