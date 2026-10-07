result = {
    'John': [85,90,78],
    'Alice': [92,88,95],
    'Bob': [75,80,82]
}

#classwork use the membership operator to check if "Alice" is in the dictionary or not
print('Alice' in result)
#classwork create a new dictionary with the same keys but with the average of the marks as values.
new_result={}

for name, marks in result.items():
    average = sum(marks) / len(marks)
    new_result[name] = average

print(new_result)
#classwork arrange the values in ascending order and print the dictionary.

for name in result:
    result[name].sort()

print(result)