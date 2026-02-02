hp = "y"
while (hp=="y"):     
    n = int(input("Enter the range: "))
    for x in range(n+1):
        if (x%5==0):
            print(x)
    hp = input("Do you want to continue?")
print("Thanks")    

