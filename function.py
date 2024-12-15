#Function "def"

def my_function():
  print("Hello from a function")

my_function()

def my_function1(text):
  print("Hello from " + text)

my_function1("Brazil")

def validation(number):
    valid = False
    if number > 10:
        valid = True
    return valid

print(validation(15))