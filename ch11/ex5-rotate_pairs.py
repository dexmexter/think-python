"""
Exercise 5

Two words are “rotate pairs” if you can rotate one of them and get the other
(see rotate_word in ch.8, Exercise 5).

Write a program that reads a wordlist and finds all the rotate pairs.
Solution: http://thinkpython2.com/code/rotate_pairs.py
"""
from rotate import rotate_word


def word_dict():
    words = {}

    with open('../words.txt') as f:
        for line in f:
            words[line.strip().lower()] = None

    return words


def rotate_pairs(word, word_dict):
    for i in range(1, 26):
        rotated = rotate_word(word, i)

        if rotated in word_dict:
            print(word, i, rotated)


if __name__ == '__main__':
    word_dict = word_dict()

    for word in word_dict:
        rotate_pairs(word, word_dict)
