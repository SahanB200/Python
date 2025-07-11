import math

# Function to check if a number is a Fibonacci number
def is_fibonacci(num):
    if num < 0:
        return False
    # Check if 5n^2 + 4 or 5n^2 - 4 is a perfect square
    def is_perfect_square(x):
        s = int(math.sqrt(x))
        return s * s == x
    return is_perfect_square(5 * num**2 + 4) or is_perfect_square(5 * num**2 - 4)

# Function to calculate prime factors
def prime_factors(n):
    factors = []
    divisor = 2
    while n > 1:
        while n % divisor == 0:
            factors.append(divisor)
            n //= divisor
        divisor += 1
        if divisor * divisor > n and n > 1:  # n is prime
            factors.append(n)
            break
    return factors

# Function to find the three smallest unique values
def find_three_smallest(nums):
    smallest1, smallest2, smallest3 = float('inf'), float('inf'), float('inf')
    for num in nums:
        if num < smallest1:
            smallest3 = smallest2
            smallest2 = smallest1
            smallest1 = num
        elif num < smallest2 and num != smallest1:
            smallest3 = smallest2
            smallest2 = num
        elif num < smallest3 and num != smallest1 and num != smallest2:
            smallest3 = num
    return smallest1, smallest2, smallest3

# Function to find the longest contiguous subsequence
def longest_contiguous_subsequence(nums):
    nums_set = set(nums)
    longest = 0
    for num in nums:
        if num - 1 not in nums_set:  # Start of a sequence
            current_num = num
            length = 1
            while current_num + 1 in nums_set:
                current_num += 1
                length += 1
            longest = max(longest, length)
    return longest

# Main program
def main():
    # Input range
    min_range = int(input("Enter the minimum value of the range: "))
    max_range = int(input("Enter the maximum value of the range: "))
    
    # Input 15 unique integers
    print(f"Enter 15 unique integers between {min_range} and {max_range}:")
    nums = []
    while len(nums) < 15:
        try:
            num = int(input(f"Enter integer {len(nums) + 1}: "))
            if num < min_range or num > max_range:
                print(f"Number out of range! Please enter a number between {min_range} and {max_range}.")
            elif num in nums:
                print("Number already entered! Please enter a unique number.")
            else:
                nums.append(num)
        except ValueError:
            print("Invalid input! Please enter an integer.")
    
    # Sum of Fibonacci numbers
    fib_sum = 0  # Initialize the sum
    for num in nums:
        if is_fibonacci(num):
            fib_sum += num  # Add the Fibonacci number to the sum
    
    # Prime factors for each number
    print("\nPrime factors:")
    for num in nums:
        print(f"{num}: {prime_factors(num)}")
    
    # Three smallest unique values
    smallest1, smallest2, smallest3 = find_three_smallest(nums)
    print(f"\nThree smallest unique values: {smallest1}, {smallest2}, {smallest3}")
    
    # Longest contiguous subsequence
    longest_sequence = longest_contiguous_subsequence(nums)
    print(f"\nLength of the longest contiguous subsequence: {longest_sequence}")
    
    # Output results
    print(f"\nSum of Fibonacci numbers in the list: {fib_sum}")

# Run the program
main()