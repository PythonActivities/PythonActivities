# Create a while loop starting with i=0 to find and print all the even numbers between 1-100 including 100 

i = 0
while i <= 100 :
    if i % 2 == 0 and i != 0:
        print(i)

    i += 1


# Create another while loop starting with m=0 to find and print all the odd numbers  between 1-100 including 1.

m = 0
while m <= 100:
    m += 1
    if m % 2 != 0:  # check odd number
        if 10 <= m <= 30:  # omit numbers 10-30
            continue
        print(m)
else:
    print("Loop is over")
