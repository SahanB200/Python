def main():
    numbers = []
    
    start = int(input("Enter the starting point: "))
    end = int(input("Enter the ending point: "))
    
    print("Enter 15 integers: ")
    for i in range(15):
        while True:
            try:
                num = int(input(f"Enter number {i+1}: "))
                if num in numbers:
                    print("Number already exist")
                    continue
                elif num >= start and num <= end:
                    numbers.append(num)
                    break
                else:
                    print("Number out of range")
                    continue
            except ValueError:
                print("Invalid input. Please try again.")
                
    
main()