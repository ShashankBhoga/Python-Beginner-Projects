print("\n=== TEMPERATURE CONVERTER ===\n")
print("1. Fahrenheit ➝ Celsius")
print("2. Celsius ➝ Fahrenheit")

try:
    choice = int(input("\nEnter your choice (1 or 2): "))

    temp = float(input("Enter the temperature: "))

    if choice == 1:
        result = (temp - 32) * 5 / 9
        print(f"\nResult: {temp}°F = {round(result, 2)}°C")

    elif choice == 2:
        result = (temp * 9 / 5) + 32
        print(f"\nResult: {temp}°C = {round(result, 2)}°F")

    else:
        print("\nInvalid choice. Please select 1 or 2.")

except ValueError:
    print("\nInvalid input. Please enter numeric values only.")
