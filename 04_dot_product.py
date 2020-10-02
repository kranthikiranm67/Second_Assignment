"""
The dot product of two lists is the sum of the products of their corresponding entries.

For example, given a = [1, 2, 3] and b = [4, 5, 6], the dot product is 32, since (1 × 4) + (2 × 5) + (3 × 6) = 32.

Given two lists of integers, compute their dot product.

Example 1
Input

a = []
b = []
Output

0
Example 2
Input

a = [1, 2, 3]
b = [4, 5, 6]
Output

32
Example 3
Input

a = [1, 2, 3, 4, 5]
b = [1, 2, 3, 4, 5]
Output

55
"""

import unittest

# Implement the below function and run this file
# Return the output, No need read input or print the ouput
# See, if you can use zip


def dot_product(list1, list2):
    # code here


# DO NOT TOUCH THE BELOW CODE
class TestDotProduct(unittest.TestCase):

    def test_01(self):
        self.assertEqual(dot_product([], []), 0)

    def test_02(self):
        self.assertEqual(dot_product([1, 2, 3], [4, 5, 6]), 32)

    def test_03(self):
        self.assertEqual(dot_product([1, 2, 3, 4, 5], [1, 2, 3, 4, 5]), 55)

    def test_04(self):
        self.assertEqual(dot_product([1, 2, 3, 4, 5], [5, 2, 3, 4, 1]), 39)

    def test_05(self):
        self.assertEqual(dot_product([18, 2, 16, 6, 5, 2, 19, 19, 13],
                                     [2, 2, 6, 16, 19, 18, 19, 13, 5]), 1036)

    def test_06(self):
        self.assertEqual(dot_product([39, 40, 16, 21, 34, 21, 32, 4, 39, 34, 29, 8, 16, 13, 1, 9, 11, 3, 39, 25],
                                     [39, 4, 8, 39, 16, 39, 16, 32, 29, 34, 25, 34, 40, 21, 21, 13, 11, 9, 3, 1]), 9256)

    def test_07(self):
        self.assertEqual(dot_product([21, 71, 98, 52, 52, 97, 64, 18, 58, 8, 6, 34, 52, 92, 63, 6, 97, 18, 16, 37, 27, 62, 55, 1, 2, 50, 36, 16, 5, 24, 46, 67, 90, 9, 29, 89, 30, 41, 76, 53, 41, 3, 31, 75, 87, 45, 43, 63,
                                      34, 93, 82, 4, 30, 66, 45, 1, 59, 77, 5, 14, 2, 64, 48, 40, 25, 39, 26, 25, 68, 99, 72, 31, 2, 10, 55, 14, 62, 4, 87, 47, 92, 13, 89, 67, 6, 1, 26, 19, 88, 91, 64, 5, 39, 82, 21, 87, 48, 41, 76, 8],
                                     [99, 97, 2, 2, 2, 97, 4, 4, 6, 6, 6, 8, 8, 10, 93, 14, 91, 14, 16, 89, 89, 16, 87, 87, 18, 18, 24, 26, 87, 26, 30, 77, 30, 75, 71, 67, 34, 67, 34, 63, 63, 59, 55, 55, 53, 47, 45, 45, 36, 43, 40, 46, 48, 48, 41, 41, 41, 39, 39, 50, 52, 52, 52, 58, 37, 31, 62, 31, 62, 29, 64, 27, 64, 64, 25, 66, 68, 72, 25, 21, 76, 21, 19, 13, 76, 9, 82, 5, 82, 5, 88, 5, 3, 90, 1, 1, 92, 1, 92, 98]), 202189)


if __name__ == '__main__':
    unittest.main(verbosity=2)
