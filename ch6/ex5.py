"""Exercise 5
The greatest common divisor (GCD) of a and b is 
the largest number that divides both of them with 
no remainder.

One way to find the GCD of two numbers is based 
on the observation that if r is the remainder when 
a is divided by b, then gcd(a, b) = gcd(b, r). As a 
base case, we can use gcd(a, 0) = a.

Write a function called gcd that takes parameters a 
and b and returns their greatest common divisor.
"""

def gcd_recursive(a, b):
    """ Determines the Greatest Common Divison of two numbers
    using recursion
    """
    print(a, b)
    if b == 0:
        return a 
    return gcd_recursive(b, a % b)

def gcd(a, b):
    """ Determines the Greatest Common Divisor of two numbers
    using a loop
    """
    result = 1
    test = 1
    while test <= a or test <= b:
        if a % test == 0 and b % test == 0:
            result = test
        test += 1

    return result

print(gcd_recursive(16, 25))