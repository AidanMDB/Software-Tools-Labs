# ######################################################
# Author : Aidan Dannhausen-Brun
# email : adannhau@purdue.edu
# ID : ee364a10
# Date : 3/3/2024
# ######################################################

import unittest
import sys
sys.path.insert(0, "./")
import main as task

# ######################################################
# No Module - Level Variables or Statements !
# ONLY FUNCTIONS BEYOND THIS POINT !
# ######################################################


class TestSuite(unittest.TestCase):

    def test_isPrime(self):
        
        with self.subTest(name="Less Than 2"):
            expected = False
            actual = task.is_prime(1)
            self.assertEqual(expected, actual)

        with self.subTest(name="Is Prime"):
            expected = True
            actual = task.is_prime(7)
            self.assertEqual(expected, actual)

        with self.subTest(name="Not Prime"):
            expected = False
            actual = task.is_prime(9)
            self.assertEqual(expected, actual)


    def test_combineVariables(self):

        with self.subTest(name="Test"):
            expected = 0
            actual = task.combine_variables(2, 2)
            self.assertEqual(expected, actual)

        with self.subTest(name="negative Num"):
            expected = 0
            actual = task.combine_variables(-2, -2)
            self.assertEqual(expected, actual)


    def test_main(self):

        with self.subTest(name="int_Even int_Even"):
            expected = None
            actual = task.main(4, 4)
            self.assertEqual(actual, expected)

        with self.subTest(name="int_Odd int_Odd"):
            expected = None
            actual = task.main(9, 9)
            self.assertEqual(actual, expected)

        with self.subTest(name="int_Prime int_Prime"):
            expected = None
            actual = task.main(7, 7)
            self.assertEqual(actual, expected)

        with self.subTest(name="String String"):
            expected = None
            actual = task.main('9', '4')
            self.assertEqual(actual, expected)

        with self.subTest(name="Float Float"):
            expected = None
            with self.assertRaises(ValueError):
                task.main(9.1, 9.1)
            






# This block is optional and can be used for testing .
# We will NOT look into its content .
# ######################################################

if __name__ == '__main__':
    with open('testrun.txt', "w") as f:
        runner = unittest.TextTestRunner(f)
        unittest.main(testRunner=runner)