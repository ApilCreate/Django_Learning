# B3
# Ask the user for a sentence. Count how many times the letter a appears (both a and A).

user = input("Type a random sentence: ").strip()
count = 0

for char in user:
    if char == 'a':
        count += 1

print(count)