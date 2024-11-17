from abc import abstractmethod

class Shape:
    def __init__(self, name: str):
        self.name = name

    @abstractmethod
    def perimeter(self) -> float:
        pass
    
    @abstractmethod
    def area(self) -> float:
        pass
    
    def __str__(self) -> str:
        return f"{self.name.capitalize()} Perimeter {self.perimeter()} Area {self.area()}"
