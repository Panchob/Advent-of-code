import unittest
from main import *

class TestFFT(unittest.TestCase):
    def setUp(self):
        self.input1 = 'bvwbjplbgvbhsrlpgdmjqwftvncz'
        self.input2 = 'nppdvjthqldpwncqszvftbrmjlhg'
        self.input3 = 'nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg'
        self.input4 = 'zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw'


    def test_findFirstMarker(self):
        self.assertEqual(findFirstMarker(self.input1), 5)
        self.assertEqual(findFirstMarker(self.input2), 6)
        self.assertEqual(findFirstMarker(self.input3), 10)
        self.assertEqual(findFirstMarker(self.input4), 11)

        #Part 2
        self.assertEqual(findFirstMarker(self.input1, 14), 23)
        self.assertEqual(findFirstMarker(self.input2, 14), 23)
        self.assertEqual(findFirstMarker(self.input3, 14), 29)
        self.assertEqual(findFirstMarker(self.input4, 14), 26)

        



if __name__ == '__main__': 
    unittest.main() 