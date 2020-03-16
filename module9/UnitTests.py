# This program is to demistrate a simple function and unit tests around it, utilizing the unittests module library.
# Joshua Snyder 03/15/2020

import unittest

def main(inputValue):
    print("Simple test for equals")
    print(str(inputValue + 2))
    return (inputValue + 2)

# Execute
main(2)

# Simple test class
class SimpleTests(unittest.TestCase):
    def testTwoPlusTwoShouldReturnFour(self):
        self.assertEqual(main(2),4)
    def testFourPlusTwoShouldNotReturnFour(self):
        self.assertNotEqual(main(4),4)