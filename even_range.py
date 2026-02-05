ev = "y"
while (ev=="y"):
    val = int(input("Enter a number: "))
    for x in range(val + 1):
        if x % 2 == 0:
            print(x)
    ev = input("Do you want to continue? ")
print("Thanks")
