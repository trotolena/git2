def palindrome():
    return s == s[::-1]


s = str(input("Type the word: "))
if s == s[::-1]:
    print("This is palindrome word")
else:
    print("This is not palindrome word")
