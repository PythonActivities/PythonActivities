# Modify the above code to run without exception and get the output.

x = 20

try:
    print(x)

except:
    print("something went wrong")

finally:
    print("The 'try except' is finished")   


# Create a variable named x with -5.  Write a condition to check whether the value is negative. If so, raise an exception as “Numbers below zero are not accepted” 

x = -5

try:
    if x < 0:
        raise ValueError("Numbers below zero are not accepted")
    print(x)

except ValueError as e:
    print(e)

except :
    print("something went wrong")


finally:
    print("The 'try except' is finished")   
