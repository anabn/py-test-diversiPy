from program.shape import Shape
from program.shapeType import ShapeType

class Square(Shape):
    def __init__(self, side):
        self.side = side
    
    def perimeter(self) -> float:
        return 4 * self.side
    
    def area(self) -> float:
        return self.side ** 2
    
    def description(self) -> str:
        return f"{ShapeType.SQUARE.value} Perimeter {self.perimeter()} Area {self.area()}"
    