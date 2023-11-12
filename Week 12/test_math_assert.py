# math_assert_test.py

import math_assert

# Test addition function
def test_addition():
    assert math_assert.addition(3, 2) == 5
    assert math_assert.addition(-1, 1) == 0
    assert math_assert.addition(0, 0) == 0

# Test subtract function
def test_subtract():
    assert math_assert.subtract(3, 2) == 1
    assert math_assert.subtract(1, 3) == -2

# Test multiply function
def test_multiply():
    assert math_assert.multiply(3, 2) == 6
    assert math_assert.multiply(0, 5) == 0

if __name__ == "__main__":
    test_addition()
    test_subtract()
    test_multiply()
