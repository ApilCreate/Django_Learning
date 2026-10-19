# C2
# Given marks = [78, 45, 92, 66, 88, 59], print the highest mark, the lowest mark, the total, and the average. Then print the list sorted in ascending and descending order.

marks = [78, 45, 92, 66, 88, 59]
print("Highest Marks: ", max(marks))
print("Lowest Marks: ", min(marks))
print("Total Marks: ", sum(marks))
print("Average Marks: ", round(sum(marks) / len(marks),2))
print("Ascending Order: ", sorted(marks))
print("Descending Order: ", sorted(marks, reverse=True))