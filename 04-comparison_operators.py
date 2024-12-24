#Comparison
#Results in boolean values True and False

x = 1
y = 2

print(x == y) #Equal
print(x != y) #Different
print(x > y) #Greater than
print(x >= y) #Greater than or equal to
print(x < y) #Less than
print(x <= y) #Less than or equal to

print(x < 2 and y == 2) #Returns true if all comparisons are True
print(x < 2 or y != 2) #Returns true if at least one comparisons are True
print(not(x < 2 or y != 2)) #Reverse the True or False
