def isprime(num):
    for i in range(2,num-1):
        if num % i == 0:
            print(num,'is not prime number')
            break
    else:
            print(num,'is prime number')

isprime(10)