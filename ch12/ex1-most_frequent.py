"""
Exercise 1

Write a function called most_frequent that takes a string and prints the
letters in decreasing order of frequency. Find text samples from several
different languages and see how letter frequency varies between languages.
Compare your results with the tables at
http://en.wikipedia.org/wiki/Letter_frequencies.

Solution:
http://thinkpython2.com/code/most_frequent.py.
"""


def frequency(t):
    t = t.lower().replace(" ", "")

    freq = dict()

    for i in t:
        if i in freq:
            freq[i] += 1
        else:
            freq[i] = 1

    return freq


if __name__ == '__main__':
    print(frequency("Hello world.")
