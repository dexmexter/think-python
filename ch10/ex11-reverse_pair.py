# -*- coding: utf-8 -*-
"""
Exercise 11

Two words are a “reverse pair” if each is the reverse of the other. Write a
program that finds all the reverse pairs in the word list.
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

def reverse_pair(words):
    result = []

    for i in words:
        if i[::-1] != i:
            if in_bisect(words, i[::-1]):
                if i[::-1] not in result:
                    result.append(i)

    return result

words = word_list("words.txt")

print(reverse_pair(words))
print(len(reverse_pair(words)))
