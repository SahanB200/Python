def add(num1, num2, num3):
    total = num1 + num2 + num3
    return total
def multiply(num1, num2):
    pro = num1 * num2
    return pro
def avg(num1, num2, num3):
    total = num1 + num2 + num3
    avg = total / 3
    return avg
def large(num1, num2):
    if num1 < num2:
        return num2
    else:
        return num1
def perimeter(width, height):
    peri = (width * height) / 2
    return peri
def f2c(temp):
    celcius = (temp - 32) * 5/9
    return celcius
def prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5)+1):
        if num % i == 0:
            return False
        else:
            return True
        
print(add(2,3,5))
print(multiply(2,3))
print(avg(2,3,5))
print(large(2,3))