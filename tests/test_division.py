import unittest
from functions import division

class TestDividir(unittest.TestCase):
    def test_dividir(self):
        self.assertEqual(division.dividir(6, 2), 3)
        self.assertEqual(division.dividir(9, 3), 3)
        self.assertEqual(division.dividir(15, 3), 5)

if __name__ == '__main__':
    unittest.main()