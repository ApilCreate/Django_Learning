# F8
# Write a function `simple_interest(principal, rate, time=1)` with a default value for `time`. Call it once with all three values and once with only two.

def simple_interest(principal, rate, time=1):
    return principal * rate * time / 100
print(simple_interest(10000, 5, 2))
print(simple_interest(10000, 5))
