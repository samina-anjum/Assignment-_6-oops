
from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    
    def area(self):
        pass
class Ractagle(Shape):
    def __init__(self,width ,height):
        self.width=width
        self.height=height
        def aera(self):
             return self.width*self.height
rect= Ractagle(5,6)
print(rect.area())      
            
            

    
        