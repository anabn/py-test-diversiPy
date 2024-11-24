from program.shapeType import ShapeType
from .rectangle import Rectangle

class Square(Rectangle):
    
    def __init__(self, side: any):
        default_top_right = (0, 0)
        default_top_left = (side, side)
        super().__init__(default_top_right, default_top_left)
        self.name = ShapeType.SQUARE.value
    