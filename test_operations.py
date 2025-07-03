# pass all these test cases
# test_operations.py

#NOTE MOVE THIS FILE OUT OF TESTS

import unittest
import os
from calculatorLab.operations import add, sub, mul, div
from calculatorLab.utils import log_call

def test_add():
    assert add(3, 4) == 7

def test_sub():
    assert sub(10, 5) == 5

def test_mul():
    assert mul(2, 3) == 6

def test_div():
    assert div(8, 2) == 4

# Bonus: Test log file creation
def test_log_file_created():
    assert os.path.exists("calculator.log")

class TestOperations(unittest.TestCase):

    def test_add(self):
        self.assertEqual(add(3, 4), 7)

    def test_subtract(self):
        self.assertEqual(sub(10, 4), 6)

    def test_multiply(self):
        self.assertEqual(mul(2, 5), 10)

    def test_divide(self):
        self.assertEqual(div(10, 2), 5)

    def test_divide_by_zero(self):
        with self.assertRaises(ValueError):
            div(10, 0)

    def test_log_file_creation(self):
        # Run a function to generate logs
        add(3, 4)
        # Check if log file was created
        self.assertTrue(os.path.exists("calculator.log"))

if __name__ == '__main__':
    unittest.main()

