# C1
# Create a list foods = ["sel roti", "masu", "chiura", "achar"]. Add "dahi" at the end, insert "bara" at position 1, remove "achar", and print the final list and its length.
foods = ["sel roti", "masu", "chiura", "achar"]
foods.append("dahi")
foods.insert(1, "bara")
foods.remove("achar")
print("Final list:", foods)
print("Length:", len(foods))