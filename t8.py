# Open the file in read mode
with open("input.txt", "r") as file:
    content = file.read()

# Count the total number of characters
character_count = len(content)

# Print the result
print(f"Total number of characters in the file: {character_count}")

# Open the file in write mode
with open("greetings.txt", "w") as file:
    file.write("Hello\n")  # Write "Hello" and move to the next line
    file.write("World")    # Write "World" on the next line

print("Strings written to greetings.txt successfully!")