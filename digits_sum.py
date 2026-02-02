lp = "y"
while (lp == "y"):
    val = int(input("Enter a number: "))
    s = 0
    val1 = val
    while val1 > 0:
        val2 = val1 % 10
        val1 //= 10
        s += val2
    print("Sum of digits of the given number: ", s)
    lp = input("Do you want to continue?")
print("Thanks")
