def is_perfect(num):
    sum = 0
#     num = int(input("Enter a number: "))
    for i in range(1, num):
        if num % i == 0:
            sum = sum + i

    if num == sum:
            print(num,"is a perfect number")
    else:
            
            print(num,"is not a perfect number")

is_perfect(28)