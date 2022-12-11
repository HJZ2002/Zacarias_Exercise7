decimal = input("Enter a string of octal digits")
while decimal == "":
    print("You did not enter string of octal digits")
    decimal = input("Enter a string of octal digits")

else:
    answer = int(decimal)
    o = 1
    decimal = 0

    while answer != 0:
        remainder = answer % 10
        answer //= 10
        decimal += remainder * o

        o *= 8
print("The integer value is ", decimal)

