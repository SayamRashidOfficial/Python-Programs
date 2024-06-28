'''class object:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def __str__(self):
        return f"{self.name},{2024-age}"
    
#p1 = person('john',21)
#print(p1.name)
#print(p1.age)
age = int(input("enter year of birth:"))
obj = object('sayam',2024)
print(obj)'''

'''class car:
    def __init__(self,name,model):
        self.name=name
        self.model=model
    def __str__(self):
        return f"The car name is {self.name} and model {self.model}"
    
c1 = car('BMW',2024)
print(c1)'''



# Decorator in python
'''def decorator(fx):
    def mfx(*args, **kwargs):
        print("Good Morning")
        fx(*args, **kwargs)
        print("Thanks for using this function")
    return mfx
    
@decorator
def hello():
    print("Hello World")
@decorator
def add(a , b):
    print(a + b)

hello()
add(1 , 2)'''


'''
# inheritence in python
class A:
    def displayA(self):
        print("welcome to AUST A")

class B:
    def displayB(self):
        print("Welcome to AUST B")

class C(A,B):
    def displayC(self):
        print("Welcome to AUST C")

obj = C()
obj.displayA()
obj.displayB()
obj.displayC()
'''
#print(obj.displayB)


'''def main():
    print("This is the main function.")

def helper():
    print("This is a helper function.")

if __name__ == "__main__":
    main()'''

def add(x,y):
    return x+y
def sub(x,y):
    return x-y
def multiple(x,y):
    return  x*y
def divide(x,y):
    if y==0:
        return "Error! division by zero"
    else:
        return x/y
def calculator():
    print("Select operator")
    print("1. Add")
    print("2. substrct")
    print("3. multiply")
    print("4. divide")
    
    while True:
        choice = input("Enter choice(1/2/3/4): ")

        if choice in ('1', '2', '3','4'):
            try:
                num1=float(input("enter a first num: "))
                num2=float(input("enter a second num: "))
            except ValueError:
                print("invalid input,please enter a number")
                continue

            if choice == '1':
                print(f"{num1}+{num2} = {add(num1,num2)}")
            elif choice == '2':
                print(f"{num1}-{num2} = {sub(num1,num2)}")
            elif choice == '3':
                print(f"{num1}*{num2} = {multiple(num1,num2)}")
            elif choice == '4':
                print(f"{num1}/{num2} = {divide(num1,num2)}")
            
            next_calculation = input("Do you want to another calculation? (y/n)")
            if next_calculation != "y":
                break
        else:
            print("invalid choice,please enter a valid choice")

if __name__ == "__main__":
    calculator()