# list = [1,2,3,4,5]
# list.append(6)
# print(id(list))
# for i in range(6,6000):
#     list.append(i)

# print(id(list))

# why doesnot the id changes even if the list is increased. Id finds the memory address but why doesnot it increase or decreases.

d = {
    "a" : 1,
    "b" : 2
}
print(d.get("a"))
print(d.get("v",0))
print(d)
l = list(d)
print(l)
a = False
if "a" in d:
    a = True
print(a)
print(len(d))
t = d.pop("a")
print(t)

#difference in set and dictionary