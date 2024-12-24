"""
Ask the price of a product and how much the user paid
Print the change, the change rounded up and rounded down
If the user paid not enough, print and finish the code
"""
import math

price = float(input("Type the price of the product: "))
paid = float(input("Type the value paid for the product:  "))

if paid < price:
    print("Not enough to pay for the product.")
elif paid == price:
    print("You paid exactly the value for the product.")
else:
    difference = paid - price
    print("You paid %d and the product cost %d, so the change is %d." %(paid, price, difference))
    differenceRoundedUp = math.ceil(difference)
    differenceRoundedDown = math.floor(difference)
    print("The change is %d, the change rounded up is %d and the change rounded down is %d." %(difference, differenceRoundedUp, differenceRoundedDown))
    