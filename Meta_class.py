import datetime

class CreatedAtMeta(type):
    def __call__(cls, *args, **kwargs):
        instance = super().__call__(*args, **kwargs)
        instance.created_at = datetime.datetime.now()
        return instance

class MyClass(metaclass=CreatedAtMeta):
    def __init__(self, value):
        self.value = value

obj = MyClass(10)
print(f"Value: {obj.value}")
print(f"Created at: {obj.created_at}")
