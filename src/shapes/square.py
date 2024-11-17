from program.shape import Shape
from program.shapeType import ShapeType

class Square(Shape):
    def __init__(self, side:any):
        super().__init__(ShapeType.SQUARE.value)
        self.side = float(side)
    
    def perimeter(self) -> float:
        return 4 * self.side
    
    def area(self) -> float:
        return self.side ** 2
    