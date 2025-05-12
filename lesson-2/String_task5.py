text = input("Enter a string: ")

vowels = 0
consonants = 0
vowel_set = "aeiouAEIOU"
for i in text:
    if i in vowel_set:
        vowels += 1
    else:
        consonants += 1

print("Number of vowels:", vowels)
print("Number of consonants:", consonants)
