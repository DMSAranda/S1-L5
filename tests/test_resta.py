import unittest
from functions import resta

class TestRestar(unittest.TestCase):
    def test_restar(self):
        self.assertEqual(resta.restar(3, 2), 1)
        self.assertEqual(resta.restar(5, 1), 4)
        self.assertEqual(resta.restar(-7, 5), -12)

if __name__ == '__main__':
    unittest.main()