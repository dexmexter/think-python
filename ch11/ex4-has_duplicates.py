"""
Exercise 4

If you did Exercise 7 (ch.10), you already have a function named has_duplicates
that takes a list as a parameter and returns True if there is any object that
appears more than once in the list.

Use a dictionary to write a faster, simpler version of has_duplicates.
Solution: http://thinkpython2.com/code/has_duplicates.py.
"""


# With a for loop
def has_duplicates(t):
    seen = {}

    for i in t:
        if i in seen:
            return True
        seen[i] = True
    return False


# With a set
def has_duplicates2(t):
    return len(set(t)) < len(t)


dups = [1, 1, 1, 1]
no_dups = [1, 4, 2, 3]


print(has_duplicates(dups))
print(has_duplicates(no_dups))

print(has_duplicates2(dups))
print(has_duplicates2(no_dups))
