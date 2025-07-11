length = float(input("Enter the length: "))
width = float(input("Enter the width: "))
height = float(input("Enter the height: "))

surface_area = (((length * width)*2) + ((width * height)*2) + ((length * height)*2))
perimeter_of_the_base = (length*2) + (width*2)
volume = length * width * height

print(f"Surface area is {surface_area}\npermiter is {perimeter_of_the_base}\nvolume is {volume}")
