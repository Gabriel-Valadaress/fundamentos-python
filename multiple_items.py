# List is a collection which is ordered and changeable. Allows duplicate members.
# Tuple is a collection which is ordered and unchangeable. Allows duplicate members.
# Set is a collection which is unordered, unchangeable*, and unindexed. No duplicate members.
# Dictionary is a collection which is ordered** and changeable. No duplicate members.
# *Set items are unchangeable, but you can remove and/or add items whenever you like.
# **As of Python version 3.7, dictionaries are ordered. In Python 3.6 and earlier, dictionaries are unordered.

#Lists
myList = ["apple", "orange", "banana"]
print(myList)
print(myList[0])
print(myList[1])
print(myList[2])
print(myList[-3])
print(myList[-2])
print(myList[-1])
print(myList[0:2])
print(myList[1:3])
print(myList[:2])
print(myList[1:])

#Operators
print("apple" in myList) #True because apple is in the list
print("lemon" in myList) #False because lemon is not in the list
print("lemon" not in myList) #True because lemon is not in the list

# Change items to the list
myList[0] = "lemon" #Switch apple for lemon
print(myList)

# Add items to the list

#Append items
myList.append("apple") #Add apple in the end of the list
print(myList)

#Insert items
myList.insert(1, "blueberry") #Add blueberry in the position 1 of the list
print(myList)

#Join list
newList = ["mango", "papaya"]

#With the + operator
print(myList + newList)

#With the extend() method
myList.extend(newList) #Extend the list with the items of new list
print(myList)

#Remove items
#Remove by the value of the item
myList.remove("blueberry") #Remove blueberry
print(myList)

#Remove by the index
myList.pop(3) #Remove apple
print(myList)
del myList[0] #Remove lemon
print(myList)

#Clear list but the list still exists
myList.clear()
print(myList)

#Delete the list completely
del myList
#print(myList) ERRO

#Sort the list
myList = ["apple", "orange", "banana"]
myList.sort() #Sort alphanumerically, ascending, by default
print(myList)

myList.sort(reverse=True) #Sort alphanumerically, descending
print(myList)

#Copy the list
copyMyList = myList.copy() #OR
otherCopy = list(myList) #OR
anotherCopy = myList[:]
print(copyMyList)
print(otherCopy)
print(anotherCopy)

#The others are basically the same