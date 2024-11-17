from typing import Type
from shapes.circle import Circle
from shapes.rectangle import Rectangle
from shapes.square import Square
from program.shapeType import ShapeType

def get_info() -> str:
    return input("Enter geometrical 2D shapes with parameters: ").strip().lower()

def split_shape_data(data: str) -> list:    
    if not data:
        print("Invalid input, no info found.")
        return []
    return data.split()

def create_shape_class(shape_type: str) -> Type[object]:
    if shape_type == ShapeType.CIRCLE.value.lower():
        return Circle  
    elif shape_type == ShapeType.SQUARE.value.lower():
        return Square  
    elif shape_type == ShapeType.RECTANGLE.value.lower():
        return Rectangle  
    else:
        raise ValueError(f"Shape type {shape_type} is not recognized.")

def run():
    entered_data = split_shape_data(get_info())
    ShapeClass = create_shape_class(entered_data[0])

    shape = ShapeClass("11")
    print(entered_data)
