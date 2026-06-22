


# Get Investment Amount
investment = int(input("Enter the investment amount (greater than 0 and less than 50000): "))
while investment <= 0 or investment >= 50000:
    print("Invalid amount. Enter an investment greater than 0 and less than 50000 ")
    investment = int(input("Enter the investment amount : "))


# Get Interest Rate
interest_rate = int(input("Enter the interest rate (greater than 0 and less than 15): "))
while interest_rate <= 0 or interest_rate >= 15:
    print("Invalid rate. Enter an interest rate greater than 0 and less than 15 ")
    interest_rate = int(input("Enter annual interest rate: "))

# Get Duration in years
years = int(input("Enter the investment duration in years(greater than 0): "))
while years <= 0:
    print("Invalid duration. Enter a duration greater than 0 ")
    years = int(input("Enter investment duration in years: "))

# Years to Month Conversion
months = years * 12

# Convert Annual Interest Rate to Monthly
monthly_rate = interest_rate / 12 / 100
total = 0.0

# Compound Monthly
for month in range(1, months + 1):
    total += investment
    interest = round(total * monthly_rate, 2)
    total += interest
    
    # Check if a full year has passed
    if month % 12 == 0:
        year = month // 12
        print(f"Year {year}: ${total:.2f}")

# Final Output
print()
print(f"Investment Duration: {years} years")
print(f"Yearly Interest Rate: {interest_rate:.1f}%")
print(f"Monthly Investment Amount: ${investment:.2f}")
print(f"Total Amount of Investment After Compounding: ${total:.2f}")

print("\nCompleted by, Anthony Tristan")