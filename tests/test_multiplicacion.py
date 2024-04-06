import unittest
from functions import multiplicacion

class TestMultiplicar(unittest.TestCase):
    def test_multiplicar(self):
        self.assertEqual(multiplicacion.multiplicar(3, 2), 6)
        self.assertEqual(multiplicacion.multiplicar(5, 0), 0)
        self.assertEqual(multiplicacion.multiplicar(4, -8), -32)

if __name__ == '__main__':
    unittest.main()