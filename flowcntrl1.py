English = 83
Sinhala = 76
Maths = 66

total = English + Sinhala + Maths
avg = float(total/3)
print(total)
print(avg)

if avg <= 34:
    print("Fail")
elif avg <= 54:
    print("S Pass")
elif avg <= 64:
    print("C Pass")
elif avg <= 74:
    print("B Pass")
elif avg >= 75:
    print("A Pass")

    # ***************************************

a = 50
b = 100
c = 150

if a < b and b < c:
    print("C is the Largest")

if b < a or b < c:
    print("B is in between A and C")

print("A") if a > b else print("B")


print("Same") if a == b else print("Not Same")
