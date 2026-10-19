# E5
# Print this pattern using nested `for` loops:
# *
# * *
# * * *
# * * * *
# * * * * *

for row in range(1, 6):
    for star in range(row):
        print("*", end=" ")
    print()
