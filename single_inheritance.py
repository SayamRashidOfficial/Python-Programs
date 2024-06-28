    # Parent class
class Animal:
        def sound(self):
            print("Animal makes a sound")
    
    # Child class inheriting from Animal
class Dog(Animal):
        def sound(self):
            print("Dog barks")
    
    # Instantiate the Dog class
dog = Dog()
dog.sound()  # Output: Dog barks
