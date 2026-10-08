def check(items):
    new_set = set()
    result = []
    for item in items:
        if item not in new_set:
            new_set.add(item)
            result.append(item)
    return result

print(check([3, 1, 3, 2, 1]) )

