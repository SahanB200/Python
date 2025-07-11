#Author: Sahan Baddegama
#Date: 17th Feb 2025

#Calculate the number is less than 10 and it's odd or even

num = float(input("Enter the number: "))

if num < 10 :

    if num % 2 == 0 :
        print("Even")

    else :
        print("Odd")
        
else:
    print("Greater than 10")