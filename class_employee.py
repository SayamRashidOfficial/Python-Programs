class Employee:
    num_employees = 0 
    
    def __init__(self, name, age):
        self.name = name
        self.age = age
        Employee.num_employees += 1 
    
    @classmethod
    def count_employees(cls):
        return cls.num_employees

# Example usage
emp1 = Employee("sayam", 19)
emp2 = Employee("ali", 25)

print(f"Number of employees: {Employee.count_employees()}")
