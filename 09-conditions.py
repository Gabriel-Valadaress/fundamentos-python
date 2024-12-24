#If, else, elif

#Use the comparison operators

x = 10
y = 20

if x > y:
    print("x is greater than y")
else:
    print("x is less than or equal to y")

if x > y:
    print("x is greater than y")
elif x < y:
    print("x is less than y")
else:
    print("x is equal to y")

if x > y:
    print("x is greater than y")
else:
    if y == 20:
        print("y is equal to 20")
    else:
        print("y is less than or equal to x but different than 20")

if x < y: print("x is less than y")

print("x is greater than y") if x > y else print("x is less than y")
