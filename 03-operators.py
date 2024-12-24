#Operators

#Addition
print(1 + 5)
print ("Hello, " + "World!")
# print ("Hello, " +  1) THIS RESULTS IN ERROR

#Subtraction
print(1 - 5)
# print ("Hello, " - "Hello, ") THIS RESULTS IN ERROR

#Multiplication
print(3 * 5)

#Division
print(30 / 7)

#Floor division
print(30 // 7)

#Modulus
print(30 % 7)

#Exponentiation
print(2 ** 3)

#Bitwise AND operator
print(7 & 4)
# Bit value of 7 is 111 and Bit value of 4 is 100
# It compares 1 to 1, 1 to 0 and 1 to 0
# If it's equal returns 1, if not 0
# The 1 to 1 returns 1 and 1 to 0 returns 0
# So 111 & 100 = 100 --> 100 equals to 4 in bit

#Bitwise OR operator
print(7 | 4)
# Bit value of 7 is 111 and Bit value of 4 is 100
# It compares 1 to 1, 1 to 0 and 1 to 0
# If both numbers are 0 returns 0, if not returns 1
# The 1 to 1 returns 1 and 1 to 0 returns 1
# So 111 | 100 = 111 --> 111 equals to 7 in bit
print(4 | 4)
# So 100 | 100 = 100 --> 100 equals to 4 in bit

#Bitwise XOR operator
print(7 ^ 4)
# Bit value of 7 is 111 and Bit value of 4 is 100
# It compares 1 to 1, 1 to 0 and 1 to 0
# If the numbers are different it returns 1, otherwise it returns 0 
# The 1 to 1 returns 0 and 1 to 0 returns 1
# So 111 | 100 = 011 --> 011 equals to 3 in bit

#Bitwise NOT operator
print(~3)
# it transform 0 to 1 and 1 to 0

#There are also bitwise shifts

#Other way of operating
x = 5
x += 5
print (x)

x = 5
x -= 5
print (x)

x = 5
x *= 5
print (x)

x = 5
x /= 2
print (x)

x = 5
x //= 2
print (x)

x = 5
x %= 2
print (x)

x = 5
x **= 2
print (x)

x = 7
x &= 4
print (x)

x = 7
x |= 4
print (x)

x = 7
x ^= 4
print (x)

#Without pre defining the variables
# print(y) results in ERROR but
print(y:= 1) #Define the variable inside the print
