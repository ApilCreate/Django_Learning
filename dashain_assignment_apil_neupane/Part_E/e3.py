# E3
# Ask the user for a word and print each character on a new line along with its index, e.g. `0 -> D`.

word = input("Enter a word: ")

for index in range(len(word)):
    print(f"{index} -> {word[index]}")
