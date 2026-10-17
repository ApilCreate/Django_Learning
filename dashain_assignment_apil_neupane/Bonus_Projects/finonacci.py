# X4
# Print the first 15 numbers of the Fibonacci series (0, 1, 1, 2, 3, 5, ...) using a while loop.
a = 0
b = 1
count = 0
while count < 15:
    print(a, end=" ")
    a, b = b, a + b
    count += 1