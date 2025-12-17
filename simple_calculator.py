print("\n=== SIMPLE CALCULATOR ===\n")

operator = input("Choose an operator (+, -, *, /, **, %): ")

try:
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))

    if operator == "+":
        result = num1 + num2

    elif operator == "-":
        result = num1 - num2

    elif operator == "*":
        result = num1 * num2

    elif operator == "/":
        if num2 == 0:
            raise ZeroDivisionError("Division by zero is not allowed.")
        result = num1 / num2

    elif operator == "**":
        result = num1 ** num2

    elif operator == "%":
        if num2 == 0:
            raise ZeroDivisionError("Modulo by zero is not allowed.")
        result = num1 % num2

    else:
        raise ValueError("Invalid operator selected.")

    print(f"\nResult: {num1} {operator} {num2} = {result}")

except ValueError as ve:
    print(f"\nInput Error: {ve}")

except ZeroDivisionError as ze:
    print(f"\nMath Error: {ze}")

except Exception:
    print("\nUnexpected error occurred. Please try again.")
