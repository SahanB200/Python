#Author: Sahan Baddegama
#Date: 17th Mar 2025

#write to the file in plain text format using write() and writelines()

file = open('file.txt', 'w')
#if file.txt doesn't exist it creates the file when you open in 'w' or 'a'
#creates the file in the specified path if path is not specified then in the same
#folder as the python program that creates the file
file.write("Hello World\n")# \n moves the cursor to nextline
file.writelines(["Sahan\n", "Tharshanan\n", "Loheeshan\n", "Kavinu\n"])
file.close()

#by opening the file with the with statement I have enabled the autoflush mode
with open('file2.txt', 'a') as file:
    file.write("Hello World\n")
    file.writelines(["Sahan\n", "Tharshanan\n", "Loheeshan\n", "Kavinu\n"])
#when the program execution exits the block it automatically closes the file
print("Write to the file is successfully completed!!!")



#read from the file using read() method
file = None
try:
    file = open("file.txt")# open the file in the read mode
    # if the "text.txt" doesn't exist when you open the file in read mode it will raise an FileNotFoundError
except FileNotFoundError:
    print("File doesn't exist. Please check!")
else:
    content = file.read()
    print("Content of the file is\n", content)
finally:
    if file is not None:
        file.close()
        
        
#read from the file using read(no_of_character) method
file = None
try:
    file = open("file.txt")# open the file in the read mode
    # if the "text.txt" doesn't exist when you open the file in read mode it will raise an FileNotFoundError
except FileNotFoundError:
    print("File doesn't exist. Please check!")
else:
    content = file.read(10)
    print("Content of the file is\n", content)
    content = file.read(10)
    print("Content of the file is\n", content)
    content = file.read(10)
    print("Content of the file is\n", content)
finally:
    if file is not None:
        file.close()

#read from the file using readline() method
file = None
try:
    file = open("file.txt")# open the file in the read mode
    # if the "text.txt" doesn't exist when you open the file in read mode it will raise an FileNotFoundError
except FileNotFoundError:
    print("File doesn't exist. Please check!")
else:
    line = file.readline()
    print(line, end='')
    line = file.readline()
    print(line.strip())
    line = file.readline()
    print(line.strip())
finally:
    if file is not None:
        file.close()
        