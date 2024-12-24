#Variables store data

x = 1
print(x)

#You can redefine the variable
x = 2
print(x)
x = "variable"
print(x)

#There are variables types
x = 2
y = "type"
print(type(x))
print(type(y))

#You can specify the variables type

x = int(2)
y = 2
w = float(2)
z = str(2)
print(x)
print(y)
print(w)
print(z)
print(type(x))
print(type(y))
print(type(w))
print(type(z))

#A variable name must start with a letter or the underscore character
#A variable name cannot start with a number
#A variable name can only contain alpha-numeric characters and underscores (A-z, 0-9, and _ )
#Variable names are case-sensitive (age, Age and AGE are three different variables)
#A variable name cannot be any of the Python keywords.

x = 1
X = 2
print(x)
print(X)

#Define multiple variables in a single line
x, y, z = 1, 2, 3
print(x)
print(y)
print(z)

x = y = z = "same value"
print(x)
print(y)
print(z)

#print in one line
print(x, y, z)
