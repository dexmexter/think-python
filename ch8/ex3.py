def is_palindrome(word):
    """ Uses string indexing to determine if a word is a palindrome.
    """
    return word[::-1] == word

print(is_palindrome("banana"))
print(is_palindrome("racecar"))