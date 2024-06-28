class Animal:
    def speak(self):
        raise NotImplementedError("Subclass must implement abstract method")

class Dog(Animal):
    def speak(self):
        return "Woof!"

animal = Animal()
print("Calling speak() on Animal instance:")
try:
    print(animal.speak())
except NotImplementedError as e:
    print(e)

dog = Dog()
print("\nCalling speak() on Dog instance:")
print(dog.speak())
