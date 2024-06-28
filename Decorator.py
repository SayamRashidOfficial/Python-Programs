def log_method(func):
    def wrapper(self, *args, **kwargs):
        print(f"Calling method: {func.__name__}")
        print(f"Arguments: {args}")
        result = func(self, *args, **kwargs)
        return self  
    return wrapper

class MyClass:
    def __init__(self, value):
        self.value = value

    @log_method
    def increment(self, amount):
        self.value += amount

    @log_method
    def multiply(self, factor):
        self.value *= factor

obj = MyClass(10)
obj.increment(5).multiply(2)

print(f"Final value: {obj.value}")


