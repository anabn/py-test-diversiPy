from program.shapeType import ShapeType
from program.shape import Shape
from .rectangle import Rectangle

class Square(Rectangle):
    
    def __init__(self):
        pass
    
    def initialise_shape(self, shape_data_str: str) -> "Square":
        shape_data = shape_data_str.split()
        side = shape_data[self.get_param_index_value(shape_data, "Side") + 1]
        default_top_right = (0, 0)
        default_top_left = (side, side)
        super().__init__(default_top_right, default_top_left)
        Shape.__init__(self, ShapeType.SQUARE.value)
        if float(side) < 0:
            raise ValueError(f"{side} is negative")
        
        return self
    