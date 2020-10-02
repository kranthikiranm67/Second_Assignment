"""
This is an exercise for you to run the files in this folder.

No code changes are required in this file, just RUN python.

You should get the output as below:
test_01 (__main__.TestRunThis) ... ok
test_02 (__main__.TestRunThis) ... ok
test_03 (__main__.TestRunThis) ... ok
test_04 (__main__.TestRunThis) ... ok
test_05 (__main__.TestRunThis) ... ok

----------------------------------------------------------------------
Ran 5 tests in 0.001s

OK
"""

import unittest

# The below function returns the arguments


def run_this(args):
    # pass
    return args


# DO NOT TOUCH THE BELOW CODE
class TestRunThis(unittest.TestCase):

    def test_01(self):
        self.assertEqual(run_this(1), 1)

    def test_02(self):
        self.assertEqual(run_this('this is a string'), 'this is a string')

    def test_03(self):
        self.assertEqual(run_this([1, 2, 9]), [1, 2, 9])

    def test_04(self):
        self.assertEqual(run_this((7, 3, 8)), (7, 3, 8))

    def test_05(self):
        self.assertEqual(run_this(set()), set())


if __name__ == '__main__':
    unittest.main(verbosity=2)
