def Character_check(x):
    if x.islower():
        return "Lowercase"

    elif x.isupper():
        return "Uppercase"

    elif x.isdigit():
        return "Digit"

    else:
        return "Special Character"

Character = input("Enter any character: ")
category = Character_check(Character)
print(f"'{Character}' is a {category}")

