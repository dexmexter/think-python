def has_duplicates(t):
    check = []
    for i in t:
        if i in check:
            return True
        check.append(i)
    return False

print(has_duplicates([1, 2, 3, 4]))
print(has_duplicates([1, 2, 4, 4]))