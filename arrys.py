wild = ["Tiger", "Lion", "Elephant", "Zebra", "Giraffe"]

#Print the value of the second item in the array. 
print(wild[1])

# Change the 3rd item as “Bear” 
wild[2] = "Bear"
print(wild)

#Append “Deer” and “Monkey” to the array.
wild.append("Deer")
wild.append("Monkey")
print(wild)

# Use pop() and remove the 2nd item in the array.
wild.pop(1)
print(wild)

# Remove “Giraffe”
wild.remove("Giraffe")
print(wild)

# Finally print the length and all the elements in the array
print(len(wild))