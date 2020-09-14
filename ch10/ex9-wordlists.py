"""
Exercise 9

Write a function that reads the file words.txt and builds a list with one
element per word. Write two versions of this function, one using the append
method and the other using the idiom t = t + [x]. Which one takes longer to
run? Why?
"""
from time import time

def word_list(file_in):
    words = []

    with open(file_in) as f:
        for line in f:
            line = line.strip()
            words.append(line)
            #if line == "abandon":
            #    break
    return words

def word_list2(file_in):
    words = []

    with open(file_in) as f:
        for line in f:
            line = line.strip()
            words = words + [line]
            if line == "date":
                break
    return words

t0 = time()
word_list("words.txt")
t1 = time()
print("function 1 takes {}".format(t1-t0))

t0 = time()
word_list2("words.txt")
t1 = time()
print("function 2 takes {}".format(t1-t0))
# fuction 2 takes much longer b/c it is recreating the list every time it add
# an item
