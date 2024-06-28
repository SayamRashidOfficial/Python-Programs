import math

def gcd(a, b):
    return math.gcd(a, b)

num1 = 12
num2 = 15
print(f"GCD of {num1} and {num2} is: {gcd(num1, num2)}")


def lcm(a, b):
    return (a * b) // gcd(a, b)

print(f"LCM of {num1} and {num2} is: {lcm(num1, num2)}")
