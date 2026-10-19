# C3
# Create a tuple dashain_days = ("Ghatasthapana", "Fulpati", "Maha Ashtami", "Maha Navami", "Vijaya Dashami"). 
# Print the first and last day, the number of days, and check whether "Fulpati" is in the tuple. 
# In a comment, explain why trying to change an item in a tuple gives an error.

dashain_days = ("Ghatasthapana", "Fulpati", "Maha Ashtami", "Maha Navami", "Vijaya Dashami")
print(f"First Day: {dashain_days[0]}\n Last Day: {dashain_days[len(dashain_days)-1]}")
print(f"Number of Days: {len(dashain_days)}")
if "Fulpati" in dashain_days:
    print(True)
else: print(False)
# dashain_days[0] = "Day1"
# print(dashain_days)
# TypeError: 'tuple' object does not support item assignment

# Here an error occured because tuple is known for its inmutability feature, which means elements cannot be reassigned,
# although they can be accessed using indexing, slicing, and loops.