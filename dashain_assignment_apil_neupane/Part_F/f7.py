# F7
# Write a function `calculate_dakshina(age)` that returns how much dakshina a relative gives: Rs. 1001 if age is below 10, Rs. 501 if age is 10-17, and Rs. 101 if 18 or above. Test it with ages 7, 15, and 25.

def calculate_dakshina(age):
    if age < 10:
        return 1001
    elif age <= 17:
        return 501
    else:
        return 101

print(calculate_dakshina(7))
print(calculate_dakshina(15))
print(calculate_dakshina(25))
