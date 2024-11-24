import pytest
from shapes.square import Square

def test_perimeter():
    test_square = Square(3)
    assert test_square.perimeter() == 12

def test_area():
    test_square = Square(5)
    assert test_square.area() == 25

def test_zero_dimensions():
    test_square = Square(0)
    assert test_square.area() == 0
    assert test_square.perimeter() == 0
    
def test_figure_name():
    assert str(Square(3)) == "Square Perimeter 12.0 Area 9.0"
    
# def test_negative_dimensions():
#     test_square = Square(-5)
#     assert test_square.area() == 4
#     assert test_square.perimeter() == 8
    