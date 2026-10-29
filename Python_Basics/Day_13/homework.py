sqaures = {n: n**2 for n in range(1,5)}
print(sqaures)

prices = {"tea": 50, "coffee": 120, "juice": 90}
cheap = {k:v for k,v in prices.items() if v<100 }
print(cheap)

names = ["Asha","Ram"]
marks = [80,90]
report = {
    n:m for n, m in zip(names, marks)
}
print(report)

# Dict Comprehensions

# 1: Map each number from 1 to 3 to its cube
nums = range(1,4)
cubes = {n : n**3 for n in nums}
print(cubes)

# 2: Swap the keys and values of this dict.
codes = {"a": 1, "b":2}
swap = {v:k for k,v in codes.items()}
print(swap)

# 3: Keep only the students who scored 40 or more
marks = {"Asha": 82, "Ram": 35, "Sita": 67}
result = {n:m for n,m in marks.items() if m>=40}
print(result)


# Set Comprehensions
nums = [11,1,1,2,2,3,3,3,3]
unique = {n for n in nums}
print(unique)

emails = ["Asha@x.com", "asha@x.com", "ram@x.com"]
clean = {e.lower() for e in emails}
print(clean)

words = ["hi", "python", "code", "hi"]
lengths = {len(w) for w in words if len(w)>2}
print(lengths)

# 1: Collect unique first letters of these words
words = ["apple", "avocado", "banana"]
one = {word[0] for word in words}
print(one)

# 2: Find every remainder when 0 to 9 is divided by 3
nums = range(10)
remainder = {num % 3 for num in nums}
print(remainder)

# 3: Find vowels that appear in a word
word = "programming"
vowels = {v for v in word if v in "aeiou"}
print(vowels)

# Ternary Operator

# 1: Label a person "Adult" if 18 or older, otherwise "Minor"

age = 17
validate = {"Adult" if age >= 18 else "Minor"}
print(validate)

# 2: Pick the larger of two numbers without max()
a,b = 8,12
large = {f"A: {a} is larger than B" if a>b else f"B: {b} is larger than A" }
print(large)

# 3: Give 10% off when the bill is over 1000
total = 1500
grand_total = total * 0.9 if total > 1000 else total
print(grand_total)