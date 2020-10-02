"""
You are given a list of integers nums, representing a decimal number
and nums[i] is between [0, 9].

For example, [1, 3, 9] represents the number 139.

Return the same list in the same representation except 
modified so that 1 is added to the number.


Example 1
Input
nums = [1, 9, 1]

Output
[1, 9, 2]

Example 2
Input
nums = [9]

Output
[1, 0]
"""

import unittest

# Implement the below function and run this file
# Return the output, No need read input or print the ouput


def and_one(nums):

    # code here



# DO NOT TOUCH THE BELOW CODE
class TestAndOne(unittest.TestCase):

    def test_01(self):
        self.assertEqual(and_one([1, 9, 1]), [1, 9, 2])

    def test_02(self):
        self.assertEqual(and_one([9]), [1, 0])

    def test_03(self):
        self.assertEqual(and_one([1, 9]), [2, 0])

    def test_04(self):
        self.assertEqual(and_one([1, 3, 9]), [1, 4, 0])

    def test_05(self):
        self.assertEqual(and_one([1, 6, 9, 9, 9]), [1, 7, 0, 0, 0])

    def test_06(self):
        self.assertEqual(and_one([9, 9, 9]), [1, 0, 0, 0])

    def test_07(self):
        self.assertEqual(and_one([9, 2, 9, 9, 9, 9, 9, 9]), [
                         9, 3, 0, 0, 0, 0, 0, 0])

    def test_08(self):
        self.assertEqual(
            and_one([9, 9, 9, 9, 9, 9, 9, 9, 0, 9, 9, 9, 9, 9, 9, 9, 9]), [9, 9, 9, 9, 9, 9, 9, 9, 1, 0, 0, 0, 0, 0, 0, 0, 0])


if __name__ == '__main__':
    unittest.main(verbosity=2)
