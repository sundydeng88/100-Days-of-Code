print("Welcome to the tip calculator.")

bill = float(input("What was the total bill? $"))

tip = int(input("What percentage tip would you like to give? 10, 12, or 15?"))

split = int(input("How many people will split the bill?"))

payment = ((bill * tip / 100) + bill) / split

print("each person should pay: $" "%.2f" % payment)