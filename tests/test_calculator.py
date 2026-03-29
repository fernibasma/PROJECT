import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from app.calculator import addition, multiplication

def test_addition():
    assert addition(2, 3)
    assert addition(-6, 1)
    assert addition(0, 0)

def test_multiplication():
    assert multiplication(2, 6)
    assert multiplication(4, 3)
    assert multiplication(0, 2)