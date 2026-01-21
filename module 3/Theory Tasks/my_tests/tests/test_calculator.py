import pytest
from calculator import add, subtract, multiply, divide

def test_add():
    assert add(2, 3) == 5

def test_add_negative():
    assert add(-2, -3) == -5

def test_subtract():
    assert subtract(10, 3) == 7

def test_multiply_pos():
    assert multiply(2, 3) == 6

def test_multiply_zero():
    assert multiply(0, 3) == 0

def test_multiply_neg():
    assert multiply(-1, 3) == -3

def test_divide_pos():
    assert divide(10, 2) == 5

def test_divide_pos_both_neg():
    assert divide(-10, -2) == 5

def test_divide_pos_one_neg():
    assert divide(-10, 2) == -5
 
def test_divide_pos_two_neg():
    assert divide(10, -2) == -5