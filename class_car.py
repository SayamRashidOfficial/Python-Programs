class Car:
    wheels = 4
    
    def __init__(self, make, model):
        self.make = make
        self.model = model

car1 = Car("Toyota", "BMW")
car2 = Car("Honda", "Civic")

print(f"Car 1: {car1.make} {car1.model}, Wheels: {car1.wheels}")
print(f"Car 2: {car2.make} {car2.model}, Wheels: {car2.wheels}")
 