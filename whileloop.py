an = "y"
while (an == "y"):
    num = int(input("Enter the number: "))
    if (num <= 100):
        val = 1
        x = 1
        while val <= num:
            x*=val
            val+=1
        print(x)
    else:
        print(" number should be less than 100 or equal to 100")    
    an = input("Do you want to continue?")
print("Thanks")
