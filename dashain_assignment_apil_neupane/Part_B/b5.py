# B5
# Ask the user for a word and check whether it is a palindrome (reads the same backwards), e.g. level, madam. Ignore uppercase/lowercase differences.
#Palindrome checker

char = input("Enter the wordr that you want to check: ").lower()

char_reverse = char[::-1]

if char == char_reverse:
    print(f"{char} is a palindrome character")
else:
    print(f"{char} is not a palindrome character") 


