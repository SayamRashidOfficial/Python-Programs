'''class Address:
    def __init__(self,street, city , zipcode):
        self.street = street
        self.city = city
        self.zipcode = zipcode
    def __str__(self):
        return f"{self.street} {self.city} {self.zipcode}"
    
class Person:
    def __init__(self, address):
        self.address = address

    def display_address(self):
        return f"Address: {self.address}"
    
address = Address("CBH"," havelian", "22500")
person = Person(address)
print(person.display_address())'''


'''from abc import abstractmethod, ABC
import math
class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    def area(self):
        return math.pi * (self.radius ** 2)
    
class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width
    def area(self):
        return self.length * self.width
    
circle = Circle(5)
rectangle = Rectangle(3,5)

print(circle.area())
print(rectangle.area())'''


#Chainable Method
'''class Myclass:
    def __init__(self,value):
        self.value = value
    def add(self,amount):
        self.value+=amount
        return self
    def multiple(self,factor):
        self.value*=factor
        return self
    def display(self):
        print(f"current value is {self.value}")
        return self
obj = Myclass(10)
obj.add(5).multiple(2).display()'''




# mixin classes
'''class LogMixin:
    def log(self, message):
        print(f"Log: {message}")

class DatabaseMixin:
    def connect(self):
        print("Connecting to the database...")

class User(LogMixin, DatabaseMixin):
    def __init__(self, username):
        self.username = username

    def display_user(self):
        self.log(f"Displaying user {self.username}")
        print(f"User: {self.username}")

# Example usage
user = User("JohnDoe")
user.display_user()
user.connect()'''






'''class LogMixin:
    def log(self, message):
        print(f"[LOG]: {message}")

class AuthMixin:
    def authenticate(self, user):
        # Simulate authentication
        if user == "admin":
            print("User authenticated")
        else:
            print("Authentication failed")

class CacheMixin:
    def cache(self, data):
        print(f"Caching data: {data}")

class WebPage(LogMixin, AuthMixin, CacheMixin):
    def __init__(self, title, content):
        self.title = title
        self.content = content

    def display(self):
        self.log(f"Displaying page: {self.title}")
        print(f"Title: {self.title}")
        print(f"Content: {self.content}")

# Example usage
page = WebPage("Home", "Welcome to the home page!")
page.display()
page.authenticate("admin")
page.cache("home_page_data")'''


