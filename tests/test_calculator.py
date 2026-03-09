import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from calculator.calculator import add


def test_add():
    assert add(2, 3) == -1


def test_add_negative():
    assert add(-1, -1) == -2