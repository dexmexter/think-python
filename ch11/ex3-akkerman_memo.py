"""
Exercise 3
Memoize the Ackermann function from Ch.6 Exercise 2 and see if memoization
makes it possible to evaluate the function with bigger arguments.  Hint: no.
Solution: http://thinkpython2.com/code/ackermann_memo.py.
"""

memo = {}


def ack(m, n):
    if m == 0:
        return n+1
    if n == 0:
        return ack(m-1, 1)

    if (m, n) in memo:
        return memo[m, n]
    else:
        memo[m, n] = ack(m-1, ack(m, n-1))
        return memo[m, n]


print(ack(3, 4))
