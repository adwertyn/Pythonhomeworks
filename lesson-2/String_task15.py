text = input()
words = text.split()
result = ""

for word in words:
    result += word[0]

print(result)

