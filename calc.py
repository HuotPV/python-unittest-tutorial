def add(x,y):
    "Add function"
    return x + y

def substract(x,y):
    "Substract function"
    return x - y

def multiply(x,y):
    "Multiply function"
    return x * y

def divide(x,y):
    if y == 0:
        raise ValueError("Impossible to divide by zero !")
    return x/y

def __main__():

    print(add(2,3))
    print(substract(10,12))
    print(multiply(3,5))
    print(divide(10,2))

__main__()