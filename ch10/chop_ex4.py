t = [1, 2, 3, 4]

def chop(t):
    del t[0]
    del t[len(t) - 1]

chop(t)
print(t)