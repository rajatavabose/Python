fac = int(input("Enter the number: "))
if (fac <= 100):
    x = 1
    for n in range(1, fac+1):
        x*=n
    print(x)
else:
    print("number should be less than 100")    
    