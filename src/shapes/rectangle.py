from program.shape import Shape
from program.shapeType import ShapeType

class Rectangle(Shape):
    def __init__(self, top_right: tuple, bottom_left: tuple):
        super().__init__(ShapeType.RECTANGLE.value)
        x1, y1 = top_right
        x2, y2 = bottom_left
        self.length = float(y1) - float(y2)
        self.width = float(x1) - float(x2)

    def perimeter(self) -> float:
        return 2 * (self.length + self.width)
    
    def area(self) -> float:
        return self.length * self.width
    