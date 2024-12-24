'''
Request a number
Request a second number
Print the results of the 4 main operations
'''

firstNumber = float(input("Type a number: "))
secondNumber = float(input("Type a number: "))

addition = firstNumber + secondNumber
subtractionOne = firstNumber - secondNumber
subtractionTwo = secondNumber - firstNumber
multiplication = firstNumber * secondNumber
divisionOne = firstNumber / secondNumber
divisionTwo = secondNumber / firstNumber

print("The addition of %d and %d equals to %d, the subtraction of %d and %d equals to %d, the subtraction of %d and %d equals to %d, the multiplication of %d and %d equals to %d, the division of %d and %d equals to %d and the division of %d and %d equals to %d." %(firstNumber, secondNumber, addition, firstNumber, secondNumber, subtractionOne, secondNumber, firstNumber, subtractionTwo, firstNumber, secondNumber, multiplication, firstNumber, secondNumber, divisionOne, secondNumber, firstNumber, divisionTwo))
