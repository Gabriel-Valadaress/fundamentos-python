#Print in the terminal two random number, one must be between 0 and 10.

import random

number1 = str(random.randrange(0, 10))
number2 = str(random.random())

print(number1 + " " + number2)