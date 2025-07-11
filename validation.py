#Author: Sahan Baddegama
#Date: 15th Mar 2025

# Input validation function for int input and float input

"""
Parameters:
    1. message - that is what will be printed while getting the input
    2. error_message - that is what will be printed if there is an error message
"""

def int_input (message, error_message= "Invalid input. Try again", min_value= None, max_value=None):
    while True:
        try:
            number = int(input(message))
            if min_value is not None and number < min_value:
                print(f"Value cannot be less than {min_value}")
                continue
            if max_value is not None and number > max_value:
                print(f"Value cannot be greater than {max_value}")
                continue
        except:
            print(error_message)
            continue
        return number
    
def float_input (message, error_message= "Invalid input. Try again", min_value= None, max_value=None):
    while True:
        try:
            number = float(input(message))
            if min_value is not None and number < min_value:
                print(f"Value cannot be less than {min_value}")
                continue
            if max_value is not None and number > max_value:
                print(f"Value cannot be greater than {max_value}")
                continue
        except:
            print(error_message)
            continue
        return number