# -*- coding: utf-8 -*-
"""
Exercise 12

Two words “interlock” if taking alternating letters from each forms a new word.
For example, “shoe” and “cold” interlock to form “schooled”.
"""
from bisect import bisect_left

def word_list(file_in):
    words = []

    with open(file_in) as f:
        for line in f:
            line = line.strip()
            words.append(line)
    return words

def in_bisect(words_list, search_word):
    i = bisect_left(words_list, search_word)

    if i != len(words_list) and words_list[i] == search_word:
        return True

    return False

def interlock(words, word):
    evens = word[::2]
    odds = word[1::2]
    return in_bisect(words, evens) and in_bisect(words, odds)

def interlock_general(words, word, n=3):
    for i in range(n):
        inter = word[i::n]
        if not in_bisect(words, inter):
            return False

if __name__ == '__main__':
    words = word_list("words.txt")

    for i in words:
        if interlock(words, i):
            print(i, i[::2], i[1::2])

    for i in words:
        if interlock_general(words, i, 3):
            print(i, i[0::3], i[1::3], i[2::3])
