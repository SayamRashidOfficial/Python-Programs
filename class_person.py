class Person:
    def __init__(self, name, age, city):
        self.name = name
        self.age = age
        self.city = city
    
    def __str__(self):
        return f"Name: {self.name}, Age: {self.age}, City: {self.city}"

person1 = Person("sayam", 19, "abbottabad")
person2 = Person("ali", 25, "Lahor")


print("Person 1:")
print(person1)

print("\nPerson 2:")
print(person2)
