import unittest
import lib
class LibTest(unittest.TestCase):
    def test_even(self):
        self.assertEqual(lib.even(6), True)
        self.assertEqual(lib.even(4), True)
        self.assertEqual(lib.even(0), True)
        self.assertEqual(lib.even(5), False)
unittest.main(verbosity=2)
