import unittest

from day7pt2 import *


class Day7Pt2_Test(unittest.TestCase):

    def test_fib(self):
        # Arrange
        num = 10
        expected_fib = 55

        # Act
        actual_fib = fib(num)

        # Assert
        self.assertEqual(expected_fib, actual_fib)


if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)
