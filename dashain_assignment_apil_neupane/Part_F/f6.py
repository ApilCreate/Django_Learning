# F6
# Write a function `count_vowels(text)` that returns how many vowels are in the string.

def count_vowels(text):
    count = 0

    for char in text.lower():
        if char in "aeiou":
            count += 1

    return count

print(count_vowels("Dashain"))
print(count_vowels("Kathmandu"))
