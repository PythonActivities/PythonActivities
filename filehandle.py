import os

# Create and write to "myfile.txt"
file1 = open("myfile.txt", "w")
file1.write("A new file has been created.")
file1.close()

# Create and write to "mytextfile.txt"
file2 = open("mytextfile.txt", "w")
file2.write("Hello! Welcome to mytextfile.txt\n")
file2.write("This file has been created by python.\n")
file2.write("Happy weekend..!!")
file2.close()

# Delete "myfile.txt"
if os.path.exists("myfile.txt"):
    os.remove("myfile.txt")
else:
    print("myfile.txt does not exist")

# Open "mytextfile.txt" and print its content
file3 = open("mytextfile.txt", "r")
print(file3.read())
file3.close()



