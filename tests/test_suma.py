import unittest
from functions import suma

class TestSumar(unittest.TestCase):
    def test_sumar(self):
        self.assertEqual(suma.sumar(3, 2), 5)
        self.assertEqual(suma.sumar(-1, 1), 0)
        self.assertEqual(suma.sumar(-1, -1), -2)

if __name__ == '__main__':
    unittest.main()