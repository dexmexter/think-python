"""
6-digit number with last four digits being a palindrome.
Add one and last 5 numbers are a palindrome
Add one and middle four are palindrome
Add one and whole number is palindrome
"""
def is_palindrome(word):
    """ Uses string indexing to determine if a word is a palindrome.
    """
    return word[::-1] == word

def lastfour(n):
    return is_palindrome(str(n)[2:6])

def lastfive(n):
    return is_palindrome(str(n)[1:6])

def middlefour(n):
    return is_palindrome(str(n)[1:5])

def allsix(n):
    return is_palindrome(str(n)[0:6])

def cartalk2():
    answers = []
    for i in range(100000, 1000000):
        if lastfour(i) and lastfive(i + 1) and middlefour(i + 2) and allsix(i + 3):
            answers.append(i)
    return answers


print(cartalk2())