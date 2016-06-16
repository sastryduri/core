import unittest
import add

class My_tests(unittest.TestCase):

    def test_add(self):
        self.assertEqual(7, add.add(3,4))

if __name__ == '__main__':
    unittest.main()
