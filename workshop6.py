#Author: Sahan Baddegama
#Date: 23rd Mar 2025

number = int(input("Enter the number: "))
while number != 1:
    if number % 2 == 0:
        number /= 2
    else:
        number = number * 3 + 1
    print(number)