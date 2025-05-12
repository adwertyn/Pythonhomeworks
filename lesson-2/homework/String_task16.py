text = input("Enter a string: ")
remove = input("Enter character or string to remove: ")

for char in remove.split():
    text = text.replace(char, "")

print("Removed version:", text)
