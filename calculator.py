ph = "y"
while (ph == "y"):
    val1 = float(input("Enter the first number: "))
    val2 = float(input("Enter the second number: "))
    val3 = input("Enter the operation (*, +, -, /,%): ")
    if (val3 == "*"):
        mul = val1 * val2
        print("The multiplication of two numbers is:", mul)
    elif (val3 == "+"):
        add = val1 + val2
        print("The addition of two numbers is:", add)
    elif (val3 == "-"):
        sub = val1 - val2
        print("The subtraction of two numbers is:", sub)
    elif (val3 == "/"):
        div = val1 / val2
        print("The division of two numbers is:", div)
    elif (val3 == "%"):
        mod = val1 % val2
        print("The modulus of two numbers is:", mod)
    else:
        print("Invalid operation")
    ph = input("Do you want to continue? ")
print("Thanks")
