# Comprehension

nums = [-2,5,-1,8]
pos = [n for n in nums if n > 0]

# 1
nums = range(1,6)
sqaure = [n**2 for n in nums]
print(sqaure)

# 2
fruits = ["apple","banana"]
up = [n.upper() for n in fruits]
print(up)

# 3
newnums = [-2,5,-1,8]
positive = [0 if n < 0 else n for n in newnums]
print(positive)