# import ipdb; ipdb.set_trace()

def sum_all(*args):
    total = 0

    for i in args:
        total += i

    return total


print(sum_all(1, 3, 4, 5, 6, 3))
