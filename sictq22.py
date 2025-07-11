#Author:Sahan Baddegama
#Date: 15th Mar 2025

import validation

def get_input():
    numbers = []
    for count in range(12):
        number = validation.int_input(f"Enter the number {count+1}: ")
        numbers.append(number)
        
    return numbers

import math
def is_prime(number):
    prime = True
    sqrt = math.sqrt(number)
    if number in [1,2]:
        return True
    for count in range(2, int(round(sqrt)+1)):
        if number % count == 0:
            prime = False
            break
    return prime

def compute_sum_prime(numbers):
    sum_of_prime = 0
    for num in numbers:
        if is_prime(num):
            sum_of_prime += num
    return sum_of_prime

def __main__():
    numbers = get_input()
    sum_prime = compute_sum_prime(numbers)
    print(sum_prime)
    
__main__()
    