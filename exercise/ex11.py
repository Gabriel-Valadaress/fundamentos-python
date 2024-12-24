"""
Ask the price of a product and how much the user paid
Print the change
If the user paid not enough, print and finish the code
"""
# MONEY is limites by 2 decimal places
# Use funciont "def"

import math

def verifyNumber(number):
    try:
        float(number)
    except:
        print("Not a number")
        quit()
    else:
        return float(number)

def verifyMoney(money):
    moneyNumber = verifyNumber(money)
    moneyNumberTimes100 = math.floor(moneyNumber * 100)
    moneyNumberDivideBy100 = moneyNumberTimes100 / 100
    if moneyNumberDivideBy100 != moneyNumber:
        print("Not a valid money number.")
    else:
        print(f"Valid money number: {moneyNumber:.2f}")
        return moneyNumberDivideBy100

price = input("Type the price of the product: ")
priceOk = verifyMoney(price)
paid = input("Type the value paid for the product:  ")
paidOk = verifyMoney(paid)

if paidOk < priceOk:
    print("Not enough to pay for the product.")
elif paidOk == priceOk:
    print("You paid exactly the value for the product.")
else:
    difference = paidOk - priceOk
    print(f"You paid {paidOk:.2f} and the product cost {priceOk:.2f}, so the change is {difference:.2f}.")
    