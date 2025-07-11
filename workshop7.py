#Author: Sahan Baddegama
#Date: 23rd Mar 2025

import math

for i in range(2, 1001):
    sqrt = int(math.sqrt(i))  # Compute the square root of the number
    is_prime = True
    for j in range(2, sqrt + 1):  # Check divisors from 2 to sqrt(i)
        if i % j == 0:
            is_prime = False
            break  # Exit loop early if not prime
    if is_prime and str(i) == str(i)[::-1]:  # Check if number is palindromic
        print(i)