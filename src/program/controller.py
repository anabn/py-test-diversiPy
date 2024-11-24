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

def get_param_index_value(lst: any, param: str) -> int:
    if param.lower() in lst:
        index = lst.index(param.lower())
        if index ==  len(lst) - 1:
            raise ValueError(f"{param} is the last element in the list, no value after it.")
    else:
        raise ValueError(f"{param} not found in the list.")
    
    return index

def create_shape_class(shape_data: list):
    if shape_data[0] == ShapeType.CIRCLE.value.lower():
        get_radius_value = shape_data[get_param_index_value(shape_data, "radius") + 1]
        return Circle(get_radius_value)
    elif shape_data[0] == ShapeType.SQUARE.value.lower():
        return Square().initialise_shape(" ".join(shape_data))
    elif shape_data[0] == ShapeType.RECTANGLE.value.lower():
        topRight_value = (shape_data[get_param_index_value(shape_data, "TopRight") + 1], shape_data[get_param_index_value(shape_data, "TopRight") + 2])
        bottomLeft_value = (shape_data[get_param_index_value(shape_data, "BottomLeft") + 1], shape_data[get_param_index_value(shape_data, "BottomLeft") + 2])
        return Rectangle(topRight_value, bottomLeft_value)  
    else:
        raise ValueError(f"Shape type {shape_data[0]} is not recognized.")

def run():    
    shape = create_shape_class(split_shape_data(get_info()))
    print(str(shape))
