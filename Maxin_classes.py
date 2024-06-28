import json

class JSONSerializable:
    def to_json(self):
        attributes = self.__dict__
        
        json_string = json.dumps(attributes, indent=2)
        
        return json_string

class MyClass(JSONSerializable):
    def __init__(self, name, age):
        self.name = name
        self.age = age

obj = MyClass("Alice", 30)

json_data = obj.to_json()
print(json_data)
