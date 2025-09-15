def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero!")
    return a / b

# Test the calculator app
if __name__ == "__main__":
    num1 = 10
    num2 = 5
    print(f"Addition of {num1} and {num2} is {add(num1, num2)}")
    print(f"Subtraction of {num1} and {num2} is {subtract(num1, num2)}")
    print(f"Multiplication of {num1} and {num2} is {multiply(num1, num2)}")
    print(f"Division of {num1} and {num2} is {divide(num1, num2)}")