"""
Exercise 10

To check whether a word is in the word list, you could use the in operator, but
it would be slow because it searches through the words in order.

Because the words are in alphabetical order, we can speed things up with a
bisection search (also known as binary search), which is similar to what you do
when you look a word up in the dictionary (the book, not the data structure).
You start in the middle and check to see whether the word you are looking for
comes before the word in the middle of the list. If so, you search the first
half of the list the same way. Otherwise you search the second half.

Either way, you cut the remaining search space in half. If the word list has
113,809 words, it will take about 17 steps to find the word or conclude that
it’s not there.

Write a function called in_bisect that takes a sorted list and a target value
and returns True if the word is in the list and False if it’s not.
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

words = word_list("../words.txt")

print(in_bisect(words, "cat"))
