"""
Give me a word with three consecutive double letters.
"""
def tripledoubles(word):
    pass

def ex7():    
    count = 0
    fin = open('words.txt')

    for line in fin:
        if tripledoubles(line):
            print(line)
            count += 1
    print(count)
