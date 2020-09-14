def nested_sum(t):
    result = 0
    for i in t:
        if type(i) == int or type(i) == float:
            result += i
        else:
            for item in i:
                result += item
    return result

t = [[1, 2], [3], [4, 5, 6], 7]

print(nested_sum(t))