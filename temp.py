an = "y"
while (an=="y"):
    val = input("Enter the temperature identity:")
    val1 = float(input("Enter the temperature:"))
    if (val=="C"):
        F = ((val1 *9)/5)+32
        print(F)
    elif (val=="F"):
        C = ((val1 - 32)/9)*5
        print(C)
    else:
        print("You have given wrong temperature scale:")
    an = input("Do you want to continue?")
print("Thanks")
