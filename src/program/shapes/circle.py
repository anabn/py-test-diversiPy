import math
from ..shape import Shape
from ..shapeType import ShapeType

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    
    def perimeter(self) -> float:
        return 2 * math.pi * self.radius
    
    def area(self) -> float:
        return math.pi * self.radius ** 2
    
    def description(self) -> str:
        return f"{ShapeType.CIRCLE.value} Perimeter {self.perimeter()} Area {self.area()}"
    
    