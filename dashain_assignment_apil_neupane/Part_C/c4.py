# C4
# Your relatives who gave you tika: ram_family = {"Hari", "Sita", "Gopal", "Maya"}
# and sita_family = {"Maya", "Bikash", "Hari", "Anju"}. 
# Print the relatives in both families (intersection), all relatives (union), and those only in ram_family (difference).
ram_family = {"Hari", "Sita", "Gopal", "Maya"}
sita_family = {"Maya", "Bikash", "Hari", "Anju"}

print(f"Relatives in both families: {ram_family & sita_family}")
print(f"All relatives: {ram_family | sita_family}")
print(f"Only in ram_family: {ram_family - sita_family}")