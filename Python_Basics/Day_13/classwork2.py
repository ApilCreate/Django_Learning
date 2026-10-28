# Write a lambda called cube that returns a number cubed.
cube = lambda x: x**3
print(cube(3))

# Use map() with a lambda to convert Celsius to Fahrenheit.

temp = [0,25,100]
# F = C * 9/5 +32
new_temp = list(map(lambda f: f * 9/5 +32, temp))
print(new_temp)

# Use filter() with a lambda to keep names longer than 3 letters.
names = ['afsdfs','bfsdfd','cd','dfsdf','cw']
main = list(filter(lambda x: len(x) > 3, names))
print(main)


# Comprehension

nums = [1,2,3,4,5]
squared = [num**2 for num in nums]
print(squared)