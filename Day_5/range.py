value = 9
total = []
for _ in range(10):
    print(value)
    value = value + 9
    total.append(value)

final = sum(total)
print(final)