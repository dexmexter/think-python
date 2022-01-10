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
    test_string = "Hello, world"

    hist = frequency(test_string)

    sort_hist = sorted(hist.items(), key=lambda kv: kv[1], reverse=True)

    new_string = ""
    for key, value in sort_hist:
        new_string += key * value

    for i in new_string:
        print(i)
