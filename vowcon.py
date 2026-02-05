pj = "y"
while (pj=="y"):
    char = input("Enter a alphabet: ")
    if (char == 'a' or char == 'e' or char == 'i' or char == 'o' or char == 'u'):
        print("Vowel")
    else:     
        print("Consonant")
    pj = input("Do you want to continue?")      
print("Thanks")
