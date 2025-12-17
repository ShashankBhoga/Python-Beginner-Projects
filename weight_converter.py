print("\n=== WEIGHT CONVERTER ===\n")
print("1. Kilograms ➝ Pounds")
print("2. Pounds ➝ Kilograms")

try:
    choice = int(input("\nEnter your choice (1 or 2): "))
    weight = float(input("Enter the weight: "))

    if choice == 1:
        result = weight * 2.20462
        print(f"\nResult: {weight} kg = {round(result, 2)} lb")

    elif choice == 2:
        result = weight * 0.453592
        print(f"\nResult: {weight} lb = {round(result, 2)} kg")

    else:
        print("\nInvalid choice. Please enter 1 or 2.")

except ValueError:
    print("\nInvalid input. Please enter numeric values only.")
