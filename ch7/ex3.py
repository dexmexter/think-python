import math

def estimate_pi():
    k = 0.0
    last_term = 1.0
    sigma = 0
    while last_term > 1e-15:
        last_term = ((math.factorial(4.0 * k)) * (1103.0 + 26390.0 * (k)))\
        /((math.factorial(k) ** 4.0) * (396.0 ** (4.0 * k)))
        k += 1.0
        sigma += last_term
    result = ((2 * math.sqrt(2)) / 9801) * sigma
    print(1 / result)

estimate_pi()
print(math.pi)