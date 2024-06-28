from abc import ABC, abstractmethod
import math

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

class Square(Shape):
    def __init__(self, side):
        self.side = side
    
    def area(self):
        return self.side ** 2

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    
    def area(self):
        return math.pi * self.radius ** 2

square = Square(5)
print(f"Area of square with side 5: {square.area()}")

circle = Circle(3)
print(f"Area of circle with radius 3: {circle.area():.2f}")
