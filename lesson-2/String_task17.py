text = input("Enter a string: ")
vowels = "aeiouAEIOU"
result = ""

for char in text:
    if char in vowels:
        result += "*"
    else:
        result += char

print("Replaced version:", result)
