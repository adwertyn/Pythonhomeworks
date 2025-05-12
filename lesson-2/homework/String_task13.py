user_input = input("Enter a string: ")

no_spaces = ""

for character in user_input:
    if character != " ":
        no_spaces = no_spaces + character

print("String without spaces:", no_spaces)
