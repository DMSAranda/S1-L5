import unittest
from division import dividir

class TestDividir(unittest.TestCase):
    def test_dividir(self):
        self.assertEqual(dividir(6, 2), 3)
        self.assertEqual(dividir(9, 3), 3)
        self.assertEqual(dividir(15, 3), 5)

if __name__ == '__main__':
    unittest.main()