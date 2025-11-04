def my_function(fname, lname):
    print(fname," ", lname)


my_function("rukshala", "perera")
    


"""Create a function “country_function” that accept one argument as “country” with the 
default value as “Sri Lanka” and Prints “I am from XXX"""

def country_function(country = "Sri Lanka"):
    print("I am from", country)

country_function()
country_function("Sweden")
country_function("India")
country_function("Brazil")


# Create a function that accepts an integer as an argument, multiply that into 3 and returns the value. 
def Calculate(y):
    result = 3 * y
    return result

# Print the calculated values for 3,6 and 9
print(Calculate(3))
print(Calculate(6))
print(Calculate(9))


