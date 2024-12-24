# Loops

#While loop
i = 0

while i < 5:
    print(i)
    i += 1

i = 0
while i < 10:
    print(i)
    i += 1
    if i == 5:
        break

i = 0
while i < 10:
    i += 1
    if i == 5:
        continue
    print(i)

i = 0

while i < 5:
    print(i)
    i += 1
else:
    print("Loop terminou")

#for loop

fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)

for x in "banana":
  print(x)

for x in fruits:
  print(x)
  if x == "banana":
    break

for x in range(6):
  print(x)

for x in range(6):
  print(x)
else:
  print("Finally finished!")
