class Temperature:
    def __init__(self, celsius):
        self._celsius = celsius 
    
    @property
    def celsius(self):
        return self._celsius
    
    @celsius.setter
    def celsius(self, value):
        if value < -273.15:
            raise ValueError("Temperature cannot be less than -273.15°C (absolute zero)")
        self._celsius = value
    
    @property
    def fahrenheit(self):
        return self._celsius * 9/5 + 32

temp = Temperature(25) 

print(f"Celsius: {temp.celsius}")

temp.celsius = 30
print(f"Updated Celsius: {temp.celsius}")

print(f"Fahrenheit: {temp.fahrenheit}")

try:
    temp.celsius = -300
except ValueError as e:
    print(e)
