a = float(input("First number: "))
operation = input("Operation (+, -, *, /): ")
b = float(input("Second number: "))

if operation == "+":
    print(a + b)
elif operation == "-":
    print(a - b)
elif operation == "*":
    print(a * b)
elif operation == "/":
    print(a / b)
else:
    print("Unknown operation")
