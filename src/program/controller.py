from typing import Type
from shapes import circle
from shapes import rectangle
from shapes import square

from shapeType import ShapeType

def get_info() -> str:
    return input("Enter geometrical 2D shapes with parameters: ").strip().lower()

def split_shape_data(data: str) -> list:    
    if not data:
        print("Invalid input, no info found.")
        return []
    return data.split()

def create_shape_class(shape_type: str) -> Type[object]:
    if shape_type == ShapeType.CIRCLE.value.lower():
        return circle  
    elif shape_type == ShapeType.SQUARE.value.lower():
        return square  
    elif shape_type == ShapeType.RECTANGLE.value.lower():
        return rectangle  
    else:
        raise ValueError(f"Shape type {shape_type} is not recognized.")

def run():
    entered_data = split_shape_data(get_info())
    ShapeClass = create_shape_class(entered_data[0])

    shape = ShapeClass(entered_data[-1])
    print(entered_data)
