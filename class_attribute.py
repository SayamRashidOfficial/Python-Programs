class Address:
    def __init__(self, street, city, zipcode):
        self.street = street
        self.city = city
        self.zipcode = zipcode

    def __str__(self):
        return f"{self.street}, {self.city}, {self.zipcode}"


class Person:
    def __init__(self, name, age, address):
        self.name = name
        self.age = age
        self.address = address

    def display_address(self):
        return f"Address: {self.address}"


address = Address("CBH", "havelian", "22500")
person = Person("sayam", 19, address)

print(person.display_address())
