import time

duplicate_list = [i % 10000 for i in range(1000000)]


# First solution
start = time.perf_counter() # 33035.9699312
# print(start)
result_list = []

for element in duplicate_list:
    if element not in result_list:
        result_list.append(element)

end = time.perf_counter() # 33105.0230519
# print(end)
time_first = end - start 
# print(time_first) #34.35...

print("First solution:", time_first, "seconds")


# Second solution
start = time.perf_counter() # 33372.27...
# print(start)

result_list = []
second_set = set()

for element in duplicate_list:
    if element not in second_set:
        second_set.add(element)
        result_list.append(element)

end = time.perf_counter() # 33372.339...
# print(end) 

time_second = end - start
# print(time_second) # 0.0607...
print("Second solution:", time_second, "seconds")


# # Difference
difference = time_first - time_second

print("Time difference:", difference, "seconds") # 27.767