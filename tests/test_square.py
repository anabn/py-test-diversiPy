import pytest
from shapes.square import Square

def test_perimeter():
    test_square = Square().initialise_shape("Square TopRight 1 1 Side 3")
    assert test_square.perimeter() == 12

def test_area():
    test_square = Square().initialise_shape("Square TopRight 1 1 Side 5")
    assert test_square.area() == 25

def test_zero_dimensions():
    test_square = Square().initialise_shape("Square TopRight 0 0 Side 0")
    assert test_square.area() == 0
    assert test_square.perimeter() == 0
    
def test_figure_name():
    assert str(Square().initialise_shape("Square TopRight 0 0 Side 3")) == "Square Perimeter 12.0 Area 9.0"
       
def test_negative_dimensions():
    negative_side = -5
    with pytest.raises(ValueError, match=f"{negative_side} is negative"):
        Square().initialise_shape(f"Square TopRight 0 0 Side {negative_side}")

def test_initialise_class():
    init_shape = Square()
    init_shape.initialise_shape("Square TopRight 1 1 Side 1")
    assert str(init_shape) == "Square Perimeter 4.0 Area 1.0"
    