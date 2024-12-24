#Validations
#Ask a number and verify if the number is integer

number = float(input("Type a number: "))
numberValidation = float(number // 1)

if numberValidation != number:
    print("The number isn't integer")
else:
    print("The number is integer")