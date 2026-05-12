price1 = float(input("Enter the price of book 1: "))
price2 = float(input("Enter the price of book 2: "))
price3 = float(input("Enter the price of book 3: "))

average = (price1 + price2 + price3) / 3

if average > 100:
    print(f"Average price: ${average:.2f} - too expensive")
else:
    print(f"Average price: ${average:.2f} - Okay")
