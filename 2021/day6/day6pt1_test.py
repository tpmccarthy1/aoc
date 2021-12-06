import unittest

from day6pt1 import *

class Day6Pt1_Test(unittest.TestCase):

    def test_reproduce(self):
        # Arrange
        test_all = {
            8: 0,
            7: 0,
            6: 5,
            5: 0,
            4: 3,
            3: 0,
            2: 2,
            1: 0,
            0: 0
        }

        expected_all = {
            8: 0,
            7: 0,
            6: 0,
            5: 5,
            4: 0,
            3: 3,
            2: 0,
            1: 2,
            0: 0
        }

        # Act
        reproduce(test_all)

        # Assert
        self.assertDictEqual(expected_all, test_all)


if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)
