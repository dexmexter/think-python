def str_pad(n, pad):
    """ Gives n as a string with pad digits. Used for checking single digit
    reversals. ex. 4 should be equal to the reverse of 40.

    n: int
    pad: int

    output: str 
    """
    return str(n).zfill(pad)

def is_reverse(x, y):
    """ Returns True if y is the reverse of x. 

    x: int
    y: int

    output: bool
    """
    return str_pad(str(x), 2) == str_pad(str(y)[::-1], 2)

def reversal_count(diff, flag = False):
    """ Gives a number of times a daughter and mothers ages will be reversed
    given a certain age difference.

    diff: int

    output: int (count of reversals)
    """
    daughter = 0
    count = 0
    mother = daughter + diff

    while mother < 120:
        if is_reverse(daughter, mother) or is_reverse(daughter, mother + 1):
            if flag:
                print(daughter, mother)
            count += 1
        daughter += 1
        mother += 1
    return count

def test_diffs():
    best_count = 0
    best_diff = 0
    for i in range(10, 80):
        if reversal_count(i) > 0:
            if reversal_count(i) > best_count:
                best_count = reversal_count(i)
                best_diff = i
    print("Best difference: %d   Best count: %d" %(best_diff, best_count))
    return best_diff

print(reversal_count(test_diffs(), True))