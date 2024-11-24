from abc import abstractmethod

class Shape:
    
    def __init__(self, name: str):
        self.name = name
        
    @abstractmethod
    def initialise_shape(self, shape_data: list):
        pass

    @abstractmethod
    def perimeter(self) -> float:
        pass
    
    @abstractmethod
    def area(self) -> float:
        pass
    
    def __str__(self) -> str:
        return f"{self.name.capitalize()} Perimeter {self.perimeter()} Area {self.area()}"

    @staticmethod
    def get_param_index_value(lst: any, param: str) -> int:
        lower_list = [i.lower() for i in lst]
        if param.lower() in lower_list:
            index = lower_list.index(param.lower())
            if index ==  len(lower_list) - 1:
                raise ValueError(f"{param} is the last element in the list, no value after it.")
        else:
            raise ValueError(f"{param} not found in the list.")
        
        return index
    