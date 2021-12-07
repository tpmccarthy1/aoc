import unittest

from day7pt1 import *


class Day7Pt1_Test(unittest.TestCase):

    def test_find_minimum(self):
            # Arrange
        nums = [16, 1, 2, 0, 4, 2, 7, 1, 2, 14]

        # Act
        minimum = find_minimum(nums)

        # Assert
        self.assertEqual(37, minimum)


if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)
