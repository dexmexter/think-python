"""
Exercise 6

Here’s another Puzzler from Car Talk (http://www.cartalk.com/content/puzzlers):

    This was sent in by a fellow named Dan O’Leary. He came upon a common
    one-syllable, five-letter word recently that has the following unique
    property. When you remove the first letter, the remaining letters form
    a homophone of the original word, that is a word that sounds exactly
    the same. Replace the first letter, that is, put it back and remove the
    second letter and the result is yet another homophone of the original
    word. And the question is, what’s the word?

    Now I’m going to give you an example that doesn’t work. Let’s look
    at the five-letter word, ‘wrack.’ W-R-A-C-K, you know like to
    ‘wrack with pain.’ If I remove the first letter, I am left with a
    four-letter word, ’R-A-C-K.’ As in, ‘Holy cow, did you see the rack
    on that buck! It must have been a nine-pointer!’ It’s a perfect
    homophone. If you put the ‘w’ back, and remove the ‘r,’ instead,
    you’re left with the word, ‘wack,’ which is a real word, it’s just
    not a homophone of the other two words.

    But there is, however, at least one word that Dan and we know
    of, which will yield two homophones if you remove either of the
    first two letters to make two, new four-letter words. The
    question is, what’s the word?

You can use the dictionary from Exercise 1 to check whether a
string is in the word list.

To check whether two words are homophones, you can use the CMU
Pronouncing Dictionary. You can download it from
http://www.speech.cs.cmu.edu/cgi-bin/cmudict or from
http://thinkpython2.com/code/c06d and you can also download
http://thinkpython2.com/code/pronounce.py, which provides a
function named read_dictionary that reads the pronouncing
dictionary and returns a Python dictionary that maps from each
word to a string that describes its primary pronunciation.

Write a program that lists all the words that solve the
Puzzler. Solution: http://thinkpython2.com/code/homophone.py.
"""


def word_dict():
    """Creates a dictionary with only five letter words from file"""
    words = {}

    with open('../words.txt') as f:
        for line in f:
            word = line.strip().lower()
            words[word] = None

    return words


def pronounce(filename='../pronunciations.txt'):
    """Returns a dictionary with the values being a primary pronounciation
    string"""
    sound_dict = dict()

    with open(filename) as f:
        for line in f:
            if line[0] == "#":
                continue

            t = line.split()

            word = t[0].lower()
            pron = ' '.join(t[1:])

            sound_dict[word] = pron

    return sound_dict


def homophone(word_a, word_b, sound_dict):
    """Takes two words and a pronounciation dictionary as input and returns
    True if the words are homophones"""
    if a not in sound_dict or b not in sound_dict:
        return False

    if sound_dict[a] == sound_dict[b]:
        return True

    return False


if __name__ == '__main__':
    word_dict = word_dict()
    sound_dict = pronounce()

    for word in word_dict:
        a = word[1:]
        b = word[0] + word[2:]

        a_homo = False
        b_homo = False

        if a in sound_dict:
            if homophone(word, a, sound_dict):
                a_homo = True

        if b in sound_dict:
            if homophone(word, b, sound_dict):
                b_homo = True

        if a_homo and b_homo:
            print(word, a, b)
