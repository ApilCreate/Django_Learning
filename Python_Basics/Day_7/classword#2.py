# 1
point = (4,7)
a,b = point[0], point[1]
print(a)
print(b)

# 2
days = ("Mon", "Tue", "Mon", "Wed")
print(days.count("Mon"), days.index("Wed"))

# 3
nums = (3,8,1)
max_number = nums[0]
min_number = nums[0]

for num in nums:
    if num > max_number:
        max_number = num
    elif num < min_number:
            min_number = num
    else: continue

print(max_number, min_number)

# 4 append 70 to the list inside the tuple and print the tuple. output: (10,20,[30,40,70],50,60)
# 5 between 30 and 40 elements of list insert a inner list [100,200], (10,20,[30,[100,200]40,70],50,60)
tuple = (10,20,[30,40],50,60)

tuple[2].append(70)
print(tuple)

tuple[2].insert(1, [100,200])
print(tuple)