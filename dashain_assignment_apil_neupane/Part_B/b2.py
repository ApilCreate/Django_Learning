# B2
# Given greeting = "Happy Dashain to you and your family",
# print: the first word, the last word, the first 5 characters, the last 6 characters, and the whole sentence reversed using slicing.

greeting = "Happy Dashain to you and your family"
split = greeting.split()
print(split) 
# ['Happy', 'Dashain', 'to', 'you', 'and', 'your', 'family']

print(split[0])
print(split[len(split) - 1])
print(greeting[:5])
print(greeting[-6:])
print(greeting[::-1])