#1
colors = ["red"]
colors.append("green")
print(colors)

#2
nums = [5,8,2,9]
print(f"First number is {nums[0]} and last is {nums[len(nums)-1]} ")

#3 
numss = [5,8,2,9]
print(numss[1:3])

#4
pets = ["cat", "dog"]
if "dog" in pets:
    print(True)
else: print(False)

#5
email = input("Enter your email")
if "@" not in email:
    print("Invalid email")

#6
nums = [7, 3, 9]
nums.sort()
print(len(nums))