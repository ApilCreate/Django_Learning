# # Problem 7: Use reduce() to find the largest number without max().
# numbers = [10,20,30,40,50]
# largest = 


# please use map function to uppercase all the strings inside a list
lists = ['a','b','c','d','e']
up = list(map(str.upper, lists))
print(up)

# please use filter function to filter out all the odd numbers from list
new_list = [1,2,3,4,5,6,7,8,9]
odd = list(filter(lambda x: x%2 != 0, new_list))
print(odd)

# please use reduce function to find the min number from list
from functools import reduce
naya_list = [31,44,63,65,66,22,88]
min_number = reduce(
    lambda current_minimum, number:
    current_minimum if current_minimum < number else number,
    naya_list
)
print(min_number)

