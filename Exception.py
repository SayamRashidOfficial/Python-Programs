def divide(x,y):
    try:
        result = x/y
    except ZeroDivisionError:
        print("division by zero")
    else:
        print(result)
    finally:
        print("executing finally clause")
divide(4,0)
divide(8,4)