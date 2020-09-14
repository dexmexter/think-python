# Exercise 1
def ex1():
    fin = open('words.txt')
    for line in fin:
        if len(line.strip()) > 20:
            print(line)
#ex1()

# Exercise 2
def has_no_e(word):
    for i in word:
        if i == 'e':
            return False
    return True

def ex2():
    e = 0
    no_e = 0
    fin = open('words.txt')

    for line in fin:
        if has_no_e(line):
            no_e += 1
            print(line)
        else:
            e += 1
    print((no_e / e) * 100)
#ex2()

# Exercise 3
def avoids(word, forbidden):
    for i in forbidden:
        if i in word:
            return False
    return True

def ex3():
    exclude = input('What are the forbidden letters?\n')
    count = 0
    fin = open('words.txt')

    for line in fin:
        if avoids(line, exclude):
            print(line)
            count += 1
    print(count)
#ex3()

# Exercise 4
def uses_only(word, string):
    for i in word:
        if i not in string:
            return False
    return True

def ex4():
    include = input('What are the letters to include?\n')
    count = 0
    fin = open('words.txt')

    for line in fin:
        if uses_only(line.strip(), include):
            print(line)
            count += 1\
    print(count)
#ex4()

# Exercise 5
def uses_all(word, string):
    for i in string:
        if i not in word:
            return False
    return True

def ex5():
    include = input('What are the letters to include?\n')
    count = 0
    fin = open('words.txt')

    for line in fin:
        if uses_all(line, include):
            print(line)
            count += 1
    print(count)
#ex5()

# Exercise 6
def is_abecedarian(word):
    return word.strip() == ''.join(sorted(word.strip()))

def ex6():
    count = 0
    fin = open('words.txt')

    for line in fin:
        if is_abecedarian(line):
            print(line)
            count += 1
    print(count)

#ex6()