"""
You are given an integer n consisting of digits 1, 2 and 3 and
you can flip one digit to a 3.

Return the maximum number you can make.

Example 1
Input
n = 123

Output
323

Explanation
We flip 1 to 3

Example 2
Input
n = 333

Output
333

Explanation
Flipping doesn't help.
"""


import unittest

# Implement the below function and run this file
# Return the output, No need read input or print the ouput

# This approach involves more complexity with no mathematical logic 
def flip_123(num):
    # code here


# DO NOT TOUCH THE BELOW CODE
class TestFlip123(unittest.TestCase):

    def test_01(self):
        self.assertEqual(flip_123(123), 323)

    def test_02(self):
        self.assertEqual(flip_123(333), 333)

    def test_03(self):
        self.assertEqual(flip_123(3123), 3323)

    def test_04(self):
        self.assertEqual(flip_123(33123), 33323)

    def test_05(self):
        self.assertEqual(flip_123(33223), 33323)

    def test_06(self):
        self.assertEqual(flip_123(13333333), 33333333)

    def test_07(self):
        self.assertEqual(flip_123(211111111111), 311111111111)


if __name__ == '__main__':
    unittest.main(verbosity=2)
