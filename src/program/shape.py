from abc import abstractmethod

class Shape:
    @abstractmethod
    def perimeter(self) -> float:
        pass
    
    @abstractmethod
    def area(self) -> float:
        pass
    
    @abstractmethod
    def description(self) -> str:
        pass
