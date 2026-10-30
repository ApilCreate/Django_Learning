# # 1:
# print(sum(x * x for x in range(5)))


# # 2:
# def read_lines(path):
#     with open(path) as f:
#         for line in f:
#             yield line.rstrip("\n")


# # 3:
# from itertools import chain

# print(list(chain([1, 2], [3])))


# 4:
def average(*nums):
    return sum(nums) / len(nums) if nums else 0

print(average(2,4,6))
# 5:
def receipt(customer, **items):
    print(f"Customer Name: {customer}")
    for item, price in items.items():
        print(f"{item}: {price}")
    print(f"Total: {sum(items.values())}")

receipt("Asha", tea=50, momo=150)

# 6:
def log(msg, history=None):
    if history is None:
        history = []
    history.append(msg)
    return history

print(log("hi"))

# 7:
def evens(limit):
    for number in range(0, limit + 1, 2):
        yield number

print(list(evens(10)))