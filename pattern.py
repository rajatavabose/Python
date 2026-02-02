gh = "y"
while (gh=="y"):
    val = int(input("Enter a number: "))
    x = val
    for i in range(1, x + 1):
        print("*" * i)
    gh = input("Do you want to continue?")  
    print("Thanks")   
 