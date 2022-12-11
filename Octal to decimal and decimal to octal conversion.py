number = input('Enter a decimal integer: ')
while number == "":
    print("You did not enter a decimal interger")
    number = input('Enter a decimal integer: ')
if number == 0:
    print(0)
else:
    print("Quotient Remainder Octal")

    octal = 0
    base = 1
    source = ""

    while number != 0:
        number = int(number)

        remainder = number % 8
        number //= 8
        octal = octal + remainder * base
        base *= 10
        source = str(remainder) + source

        print("%5d%8d%12s" % (number, remainder, source))

    print('The octal representation is ', octal)
