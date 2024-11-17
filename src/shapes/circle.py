import math
from program.shape import Shape
from program.shapeType import ShapeType

class Circle(Shape):
    def __init__(self, radius:any):
        super().__init__(ShapeType.CIRCLE.value)
        self.radius = float(radius)
    
    def perimeter(self) -> float:
        return 2 * math.pi * self.radius
    
    def area(self) -> float:
        return math.pi * self.radius ** 2
    