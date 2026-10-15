# A5
# Convert the list [1, 2, 2, 3, 3, 3] into a set and then into a tuple. Print the result after each step and explain in a comment what changed.

list = [1,2,2,3,3,3]
set = set(list)
#Converting list into a set
print(set) # {1, 2, 3}
tuple = tuple(set)
#Converting set into a tuple
print(tuple) # (1, 2, 3)