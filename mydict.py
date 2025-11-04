pet = {
    "name": "Sheeba",
    "age": 3,
    "breed": "German Shepherd",
    "color": "brown"
}

#pet keys
print(pet.keys())

#print the age
print(pet["age"])


# update the age
pet["age"] = 5
print("Updated pet age:", pet["age"])

# Add a new key “sound” and value “bark” 
pet["sound"] = "bark"
print("After adding sound:", pet)

# Remove the “color” key and its value
pet.pop("color")
print("After removing color:", pet)

#  values in the dictionary and print them
print("Values in dictionary:")
for value in pet.values():
    print(value)
