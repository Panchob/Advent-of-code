import unittest
from day12 import Moon, step, repeatAfter, separateAxis, allSystemRepeat

class TestNBody(unittest.TestCase):
    def setUp(self):
        self.moons1 = [Moon([-1, 0, 2]), Moon([2, -10, -7]), Moon([4, -8, 8]), Moon([3, 5, -1])]
        self.result1 = [Moon([2, -1, 1]), Moon([3, -7, -4]), Moon([1, -7, 5]), Moon([2, 2, 0])]
        self.result2 = [Moon([5, -3, -1]), Moon([1, -2, 2]), Moon([1, -4, -1]), Moon([1, -4, 2])]
        self.result3 = [Moon([-1, -9, 2]), Moon([4, 1, 5]), Moon([2, 2, -4]), Moon([3, -7, -1])]
        self.result4 = [Moon([2, 1, -3]), Moon([1, -8, 0]), Moon([3, -6, 1]), Moon([2, 0, 4])]
        self.moons2 = separateAxis([Moon([-1, 0, 2]), Moon([2, -10, -7]), Moon([4, -8, 8]), Moon([3, 5, -1])])


    def test_step(self):
        step(self.moons1, 1)
        self.assertEqual(self.moons1,  self.result1)
        step(self.moons1, 1)
        self.assertEqual(self.moons1,  self.result2)
        step(self.moons1, 3)
        self.assertEqual(self.moons1,  self.result3)


    def test_repeatAfter(self):
        self.assertEqual(allSystemRepeat(self.moons2), 2772)


if __name__ == '__main__': 
    unittest.main() 