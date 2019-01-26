t = [1, 2, 3]

def cumsum(t):
    total = 0
    result = []

    for i in t:
        total += i
        result.append(total)
    
    return result


print(cumsum(t))