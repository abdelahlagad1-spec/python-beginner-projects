def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Error: Division by zero"
    return x / y

print("Calculator")
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
op = input("Enter operation (+, -, *, /): ")

if op == '+':
    print(add(num1, num2))
elif op == '-':
    print(subtract(num1, num2))
elif op == '*':
    print(multiply(num1, num2))
elif op == '/':
    print(divide(num1, num2))
else:
    print("Invalid operation")