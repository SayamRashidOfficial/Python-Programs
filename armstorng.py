def armstrong(num):
    # num = int(input("Enter a number: "))
    order = len(str(num))
    sum = 0
    temp = num

    while temp > 0:
        digit = temp % 10
        sum += digit ** order
        temp //= 10
    
    if sum == num:
        print(f"{num} is Armstrong Number")
    else:
        print(f"{num} is not Armstrong Number")

armstrong(153)









# def isArmstrong(x):
     
#     n = order(x)
#     temp = x
#     sum1 = 0
     
#     while (temp != 0):
#         r = temp % 10
#         sum1 = sum1 + power(r, n)
#         temp = temp // 10
 
#     # If condition satisfies
#     return (sum1 == x)
 
# # Driver code
# x = 153
# print(isArmstrong(x))
 
# x = 1253
# print(isArmstrong(x))