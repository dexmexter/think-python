def histogram(s):
    d = dict()
    for letter in s:
        d[letter] = d.get(letter, 0) + 1
    return d


def print_hist(h):
    for c in h:
        print(c, h[c])


def reverse_lookup(d, val):
    for key in d:
        if d[key] == val:
            return key
    raise LookupError("That letter does not appear")


def invert_dict(d):
    inverse = dict()
    for key in d:
        val = d[key]
        if val not in inverse:
            inverse[val] = [key]
        else:
            inverse[val].append(key)
    return inverse


known = {0: 0, 1: 1}


def fibonacci(n):
    if n in known:
        return known[n]

    res = fibonacci(n-1) + fibonacci(n-2)
    known[n] = res
    return res
