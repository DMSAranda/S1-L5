import unittest
from functions import restar

class TestRestar(unittest.TestCase):
    def test_restar(self):
        self.assertEqual(restar(3, 2), 1)
        self.assertEqual(restar(5, 1), 4)
        self.assertEqual(restar(-7, 5), -12)

if __name__ == '__main__':
    unittest.main()