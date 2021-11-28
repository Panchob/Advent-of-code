import unittest
from day16 import *

class TestFFT(unittest.TestCase):
    def setUp(self):
        self.input1 = [1, 2, 3, 4, 5, 6, 7, 8]
        self.input2 = [8, 0, 8, 7, 1, 2, 2, 4, 5, 8, 5, 9, 1, 4, 5, 4, 6, 6, 1, 9, 0, 8, 3, 2, 1, 8, 6, 4, 5, 5, 9, 5]


    def test_multiphasing(self):
        self.assertEqual(multiphasing(self.input1, 4), '01029498')
        self.assertEqual(multiphasing(self.input2, 100), '24176176')

        



if __name__ == '__main__': 
    unittest.main() 