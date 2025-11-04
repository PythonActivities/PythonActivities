mytuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")

print("length of mytuple", mytuple)

print("Type ", type(mytuple))

print(mytuple[0])
print(mytuple[3])


# convert tuple into a list and add “watermelon” and convert it back to a tuple

thislist = list(mytuple)

thislist.append("watermelon")

mytuple = tuple(thislist)

print(mytuple)

# Loop through each item in the tuple and print 
for item in mytuple:
    print(item)

