import math
def __main__():
    global list1
    list1 = []
    for i in range(12):
        num = valid_input(f"Enter the number {i+1}: ")
        list1.append(num)
        prime_num()
            
    print(f"Sum of all prime numbers is {total}")
    print(f"Product of all non prime numbers is {pro}")
    sorting()
    print(list1[-1])
    while length:
        for x in reversed(list1):
            i = -2
            if x != list1[i]:
                print(list1[i])
                while list1[i] != list1[i-1]:
                    print(list1[i-1])
                    break
                i -= 1
            else:
                i -= 1
                continue
            
def valid_input(message):
    while True:
        try:
            num = int(input(message))
            return num
        except:
            print("Invalid input. Try again.")
            continue
        
def prime_num():
    global total, pro
    total = 0
    pro = 1
    for num in list1:
        if num == 2:
            total += num
        else:
            sqrt = math.sqrt(num)
            for count in range(2, round(sqrt)+1):
                if num % count == 0:
                    pro = pro * num
                    break
                else:
                    total += num
                    break
                
def sorting():
    global length
    length = len(list1)
    times = (length*(length-1))/2
    while times:
        for i in range(length-1):
            if list1[i] > list1[i+1]:
                list1[i],list1[i+1] = list1[i+1],list1[i]
        times -= 1
    print(list1)
                              
__main__()