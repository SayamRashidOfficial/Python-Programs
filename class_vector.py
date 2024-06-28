class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def __str__(self):
        return f"({self.x}, {self.y})"
    
    def __add__(self, other):
        if isinstance(other, Vector):
            return Vector(self.x + other.x, self.y + other.y)
        else:
            raise TypeError("Unsupported operand type(s) for +: 'Vector' and {}".format(type(other)))
    
    def __sub__(self, other):
        if isinstance(other, Vector):
            return Vector(self.x - other.x, self.y - other.y)
        else:
            raise TypeError("Unsupported operand type(s) for -: 'Vector' and {}".format(type(other)))

v1 = Vector(2, 3)
v2 = Vector(-1, 5)

result_add = v1 + v2
print(f"Addition result: {v1} + {v2} = {result_add}")

result_sub = v1 - v2
print(f"Subtraction result: {v1} - {v2} = {result_sub}")
