import pytest
from shapes.rectangle import Rectangle

def test_perimeter():
    rect = Rectangle((5, 3), (1, 1))
    assert rect.perimeter() == 12

def test_area():
    rect = Rectangle((6, 6), (1, 1))
    assert rect.area() == 25

def test_zero_dimensions():
    rect = Rectangle((3, 1), (3, 6))
    assert rect.area() == 0
    assert rect.perimeter() == 10

def test_negative_dimensions():
    rect = Rectangle((-1, -1), (1, 1))
    assert rect.area() == 4
    assert rect.perimeter() == 8