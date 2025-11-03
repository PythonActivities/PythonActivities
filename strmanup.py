a = "Hello, World"

b = """Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor ,
incididunt ut labore et dolore magna aliqua."""

c = "We are the so-called \"Vikings\" from the north."


#string lenght

print("length of a", len(a))
print("length of b", len(b))
print("length of c", len(c))


# 1st and 5th characters in each string
print("a -->  1st -", a[0] , "5th -", a[4])
print("b -->  1st -", a[0] , "5th -", a[4])
print("c -->  1st -", a[0] , "5th -", a[4])

# for loop 
fruit = "mango"
for letter in fruit:
    print (letter)


# 4.2
    # Check whether variable a has “world” and print relative boolean value
print("Does 'a' contain 'World'?", "World" in a)
print("Does 'b' contain 'consectetur adipisc'?", "consectetur adipisc" in a)
print("Does 'c' contain 'Vikings'?", "Vikings" in a)


#4.3
    #slice
x = b[1:4]
y = b[:4]
z = b[6:]

print("x:", x)
print("y:", y)
print("z:", z)

#4.4
#  a in upper case
print(" a into upper case", a.upper())
print(" a into lower case", a.lower())

# Remove white spaces of variable b and print.
print(b.strip)

# Replace “World” with “Globe” in variable a and print it. 
print(a.replace("World", "Globe"))

# Split variable b at comma and save it to a new variable p and print it.
p = b.split(",")

#variable concatenate
m = a + " " + b
print(m)








