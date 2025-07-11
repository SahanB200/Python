def main():
    # Step 1: Initialize the list
    numbers = []

    # Step 2: Input 12 integers
    print("Enter 12 integers:")
    for i in range(12):
        while True:
            try:
                num = int(input(f"Enter number {i + 1}: "))
                numbers.append(num)
                break  # Exit loop if input is valid
            except ValueError:
                print("Invalid input. Please enter an integer.")

    # Step 3: Compute sum of prime numbers
    prime_sum = 0
    non_prime_product = 1
    for num in numbers:
        if is_prime(num):
            prime_sum += num
        else:
            non_prime_product *= num

    # Step 4: Identify three largest unique numbers
    largest_three = find_largest_three(numbers)

    # Step 5: Print results
    print(f"Sum of prime numbers: {prime_sum}")
    print(f"Product of non-prime numbers: {non_prime_product}")
    print(f"Three largest unique numbers: {largest_three}")


# Function to check if a number is prime
def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True


# Function to find the three largest unique numbers
def find_largest_three(nums):
    unique_nums = list(set(nums))  # Remove duplicates
    largest_three = [float('-inf'), float('-inf'), float('-inf')]

    for _ in range(3):  # Find the three largest numbers
        max_num = float('-inf')
        for num in unique_nums:
            if num > max_num:
                max_num = num
        largest_three[_] = max_num
        unique_nums.remove(max_num)  # Remove the largest number after each iteration

    return largest_three


# Run the program
main()
