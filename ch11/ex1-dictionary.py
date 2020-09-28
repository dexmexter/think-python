"""
Exercise 1

Write a function that reads the words in words.txt and stores them as keys in a
dictionary. It doesn't matter what the values are. Then you can use the in
operator as a fast way to check whether a string is in the dictionary.
"""


def word_dict(file_in):
    words = {}

    with open(file_in) as f:
        for line in f:
            words[line.strip()] = None

    return words


def in_dict(d, word):
    return word in d


words = word_dict('../words.txt')

print(in_dict(words, "dog"))
