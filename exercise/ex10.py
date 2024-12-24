'''
Request a number
Verify if the user input is a valid number
Request a second number
Verify if the user input is a valid number
Print the results of the 4 main operations
'''
#ALL THE VERIFICATION MUST BE DONE TROUGH A FUNCTION "def"
import math

def verifyNumber(number):
    try:
        float(number)
    except:
        print("Not a number")
        quit()
    else:
        return float(number)

firstNumber = input("Type a number: ")
firstNumberOk = verifyNumber(firstNumber)

secondNumber = input("Type a number: ")
secondNumberOk = verifyNumber(secondNumber)

addition = firstNumberOk + secondNumberOk
subtractionOne = firstNumberOk - secondNumberOk
subtractionTwo = secondNumberOk - firstNumberOk
multiplication = firstNumberOk * secondNumberOk
divisionOne = firstNumberOk / secondNumberOk
divisionTwo = secondNumberOk / firstNumberOk

print("The addition of %d and %d equals to %d, the subtraction of %d and %d equals to %d, the subtraction of %d and %d equals to %d, the multiplication of %d and %d equals to %d, the division of %d and %d equals to %d and the division of %d and %d equals to %d." %(firstNumberOk, secondNumberOk, addition, firstNumberOk, secondNumberOk, subtractionOne, secondNumberOk, firstNumberOk, subtractionTwo, firstNumberOk, secondNumberOk, multiplication, firstNumberOk, secondNumberOk, divisionOne, secondNumberOk, firstNumberOk, divisionTwo))
