# The Ackermann function, A(m,n)

def ack(m, n):
    if m == 0:
        print("m", m, "n", n)
        n += 1
    
    if m > 0 and n == 0:
        print("m1", m, "n1", n)
        print(" ", ack(m - 1, 1))
    
    if m > 0 and n > 0:
        print("m2", m, "n2", n)
        print(". ", ack(m - 1, ack(m, n - 1)))

    return n

print(ack(2, 3))