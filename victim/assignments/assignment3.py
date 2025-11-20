def add(a, b):
    return a + b

def div(a, b):
    if b == 0:
        raise ZeroDivisionError("cannot divide by zero")
    return a / b

if __name__ == "__main__":
    print(add(3, 5))
    print(div(8, 2))
