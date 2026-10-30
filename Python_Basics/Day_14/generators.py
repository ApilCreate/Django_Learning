list = [1,2,3,4,5]
def frist_three():
    yield list

gen = frist_three()
print(gen)
for n in gen:
    print(n)

def countdown(n):
    print("Start")
    while n > 0:
        yield n
        n -= 1
    print("done")

gen = countdown(3)
# print(next(gen))
# print(next(gen))
# print(next(gen), "Finished")
print(*(next(gen) for _ in range(3)), sep="\n")
