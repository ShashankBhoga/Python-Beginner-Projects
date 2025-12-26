principle = 0
rate = 0
time = 0

while principle <= 0:
    principle = float(input("Enter the principal amount: "))
    if principle <= 0:
        print("Principal must be greater than zero. Try again.")

while rate <= 0:
    rate = float(input("Enter the interest rate (%): "))
    if rate <= 0:
        print("Interest rate must be greater than zero. Try again.")

while time <= 0:
    time = int(input("Enter the time (years): "))
    if time <= 0:
        print("Time must be at least 1 year. Try again.")

total = principle * (1 + rate/100) ** time

print(f"\nTotal amount after {time} years: {total:.2f}")
