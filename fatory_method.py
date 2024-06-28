from abc import ABC, abstractmethod

# Abstract Product: Vehicle
class Vehicle(ABC):
    @abstractmethod
    def drive(self):
        pass

# Concrete Products: Car and Bike
class Car(Vehicle):
    def drive(self):
        return "Driving a Car"

class Bike(Vehicle):
    def drive(self):
        return "Riding a Bike"

# Abstract Factory: VehicleFactory
class VehicleFactory(ABC):
    @abstractmethod
    def create_vehicle(self):
        pass

# Concrete Factories: CarFactory and BikeFactory
class CarFactory(VehicleFactory):
    def create_vehicle(self):
        return Car()

class BikeFactory(VehicleFactory):
    def create_vehicle(self):
        return Bike()

# Usage example
def test_vehicle_factory(factory):
    vehicle = factory.create_vehicle()
    print(vehicle.drive())

# Testing with CarFactory
print("Testing CarFactory:")
test_vehicle_factory(CarFactory())

# Testing with BikeFactory
print("\nTesting BikeFactory:")
test_vehicle_factory(BikeFactory())
