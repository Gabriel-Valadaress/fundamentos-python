'''
Request a number
Verify if the user input is a valid number
Request a second number
Verify if the user input is a valid number
Print the results of the 4 main operations
'''
import math

firstNumber = input("Type a number: ")

try:
    float(firstNumber)
except:
    print("Not a number")
    quit()
else: 
    firstNumberOk = float(firstNumber)

secondNumber = input("Type a number: ")

try:
    float(secondNumber)
except:
    print("Not a number")
    quit()
else: 
    secondNumberOk = float(secondNumber)

addition = firstNumberOk + secondNumberOk
subtractionOne = firstNumberOk - secondNumberOk
subtractionTwo = secondNumberOk - firstNumberOk
multiplication = firstNumberOk * secondNumberOk
divisionOne = firstNumberOk / secondNumberOk
divisionTwo = secondNumberOk / firstNumberOk

print("The addition of %d and %d equals to %d, the subtraction of %d and %d equals to %d, the subtraction of %d and %d equals to %d, the multiplication of %d and %d equals to %d, the division of %d and %d equals to %d and the division of %d and %d equals to %d." %(firstNumberOk, secondNumberOk, addition, firstNumberOk, secondNumberOk, subtractionOne, secondNumberOk, firstNumberOk, subtractionTwo, firstNumberOk, secondNumberOk, multiplication, firstNumberOk, secondNumberOk, divisionOne, secondNumberOk, firstNumberOk, divisionTwo))
