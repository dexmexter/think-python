import re
"""
Give me a word with three consecutive double letters.
"""
def tripdoub(word):
    for i in range(len(word)):
        if word[i] == word[i + 1] and \
        word[i + 2] == word[i + 3] and \
        word[i + 4] == word[i + 5]:
            return True
    return False

def regtripdoub(word):
    regex = r"((.)\2){3}"
    if re.search(regex, word):
        return True
    return False

#print(regtripdoub('Thhsaakkdkje'))


def ex7():    
    count = 0
    fin = open('words.txt')

    for line in fin:
        if regtripdoub(line):
            print(line)
            count += 1
    return count

print(ex7())