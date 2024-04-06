import unittest
from functions import multiplicar

class TestMultiplicar(unittest.TestCase):
    def test_multiplicar(self):
        self.assertEqual(multiplicar(3, 2), 6)
        self.assertEqual(multiplicar(5, 0), 0)
        self.assertEqual(multiplicar(4, -8), -32)

if __name__ == '__main__':
    unittest.main()