word = input("Enter the word: ")


if word[::-1]==word: #Check it using word[::-1] reverses word.
    print("String is palindrome. ")
else:
    print("String is not palindrome.")
