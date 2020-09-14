def birthday(n):
    result = 1.0

    for i in range(n):
        result *= (365 - i) / 365.0

    return 100 * (1 - result)


print(birthday(50))
