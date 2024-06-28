'''import phonenumbers
from phonenumbers import geocoder
phone_number1 = phonenumbers.parse("+923279850619")

#print("\nPhone Number Location\n")
print(geocoder.description_for_number(phone_number1,"en"))
'''

'''for item in range(6):
    if item == 3:
        break
    print(item)
else:
    print("Finally finished")'''

'''import heapq

# Create an empty heap
heap = []

# Push elements onto the heap
heapq.heappush(heap,10)
heapq.heappush(heap,1)
heapq.heappush(heap,5)
heapq.heappush(heap,4)


# Print the smallest element
print(heapq.heappop(heap))  # Output: 1

# Push and pop in a single statement
print(heapq.heappushpop(heap, 2))  # Output: 3

# Transform a list into a heap
data = [5, 7, 9, 3]
heapq.heapify(data)

# Print the smallest element
print(heapq.heappop(data))  # Output: 1'''


'''s = 'say'
r = s in 'my name is sayam'
print(r)'''

'''name = "John"
age = 23
print("%s is %d years old." % (name, age))'''

'''from datetime import datetime

now = datetime.now()
print(f"Current date and time: {now:%Y-%m-%d     %H:%M:%S}")'''

'''li =['milk','butter','cheez','bread']

li.pop()
del li[0]
print(li)'''

'''a = ['bacon', 'tomato', 'ham', 'lobster', 'tomato', 'ham', 'lobster']
print(a[0:6:2])'''

'''a = 3
b = 200
r = a if a > b else b
print(r)'''

'''value = True
if value is None:
    print("Value is None")
elif not value:
    print("Value is False")
else:
    print("Value is True")'''

'''primes = [2, 3, 5, 7]
for prime in primes:
    print(prime)'''


'''animals = ["dog", "cat", "mouse"]
# enumerate() adds counter to an iterable
for i, value in enumerate(animals):
    print(i, value)'''

'''x = 0
while x < 4:
    print(x)
    x += 1  # Shorthand for x = x + 1'''

'''nums = [60, 70, 30, 110, 90]
for n in nums:
    if n > 100:
        print("%d is bigger than 100" %n)
        break
else:
    print("Not found!")'''

'''words = ['Mon', 'Tue', 'Wed']
nums = [1, 2, 3]
# Use zip to pack into a tuple list
for w, n in zip(words, nums):
    print('%d:%s, ' %(n, w))'''


'''with open("myfile.txt") as file:
    for line in file:
        print(line)'''


'''class Animal:
    def __init__(self, name,age):
        self.name = name
        self.age = age
    def __str__(self):
        return f"{self.name},{self.age}"
obj = Animal('sayam',19)
print(obj)
#print(obj.name)
#print(obj.age)'''

'''values = (-x for x in [1,2,3,4,5])
gen_to_list = list(values)

# => [-1, -2, -3, -4, -5]
print(gen_to_list)'''


def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Error! Division by zero."
    else:
        return x / y

def calculator():
    print("Select operation:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")

    while True:
        choice = input("Enter choice (1/2/3/4): ")

        if choice in ('1', '2', '3', '4'):
            try:
                num1 = float(input("Enter first number: "))
                num2 = float(input("Enter second number: "))
            except ValueError:
                print("Invalid input. Please enter a number.")
                continue

            if choice == '1':
                print(f"{num1} + {num2} = {add(num1, num2)}")
            elif choice == '2':
                print(f"{num1} - {num2} = {subtract(num1, num2)}")
            elif choice == '3':
                print(f"{num1} * {num2} = {multiply(num1, num2)}")
            elif choice == '4':
                print(f"{num1} / {num2} = {divide(num1, num2)}")

            next_calculation = input("Do you want to perform another calculation? (yes/no): ")
            if next_calculation != 'yes':
                break
        else:
            print("Invalid choice. Please enter a valid choice.")

if __name__ == "__main__":
    calculator()











