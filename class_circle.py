import math

class Circle:
    def __init__(self, radius):
        self.radius = radius
    
    def calculate_area(self):
        return math.pi * self.radius ** 2

circle1 = Circle(5)  
circle2 = Circle(3)  

print(f"Circle 1 Area: {circle1.calculate_area():.2f}")
print(f"Circle 2 Area: {circle2.calculate_area():.2f}")
