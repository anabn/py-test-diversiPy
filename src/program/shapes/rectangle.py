from ..shape import Shape
from ..shapeType import ShapeType

class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width
    
    def perimeter(self) -> float:
        return 2 * (self.length + self.width)
    
    def area(self) -> float:
        return self.length * self.width
    
    def description(self) -> str:
        return f"{ShapeType.RECTANGLE.value} Perimeter {self.perimeter()} Area {self.area()}"
    