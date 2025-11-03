a = "Hello"

def     myfunc():
    global a
    print("Python is " + a)

    a = "world"
    print("Python is " + a)

myfunc()

print("Python is " + a)