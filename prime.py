ph = "y"
while (ph=="y"):    
    pri = int(input("Enter the number: "))
    if (pri%2==0):
        print("Not a prime number")
    else:
        print("Prime number")   
    ph = input("Do you want to continue?")
print("Thanks")
