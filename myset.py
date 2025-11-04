# Creating a set 
thisset = {"apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"}

# length of the set
print("Length of the set:", len(thisset))

# type of the set
print("Type of thisset:", type(thisset))

# Print all items in the set
print("Items in set:", thisset)

# Check if "banana" is present in the set
print("Is 'banana' in thisset?:", "banana" in thisset)

# Add an item to the set
thisset.add("watermelon")
print("After adding 'watermelon':", thisset)

# Remove "kiwi" from the set
thisset.remove("kiwi")
print("After removing 'kiwi':", thisset)

# Loop through the set
print("Looping through set:")
for item in thisset:
    print(item)
