a = float(input("First number: "))
operation = input("Operation (+, -, *, /): ")
b = float(input("Second number: "))

operation == "/" and b == 0 and print("Division by zero is not allowed") or (
    operation == "+" and print(a + b) or
    operation == "-" and print(a - b) or
    operation == "*" and print(a * b) or
    operation == "/" and print(a / b)
)
