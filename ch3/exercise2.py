def do_twice(func, arg):
    f(arg)
    f(arg)

def print_twice(x):
    print(x)
    print(x)

def print_spam():
    print("spam")

def do_four(func, arg):
    do_twice(func, arg)
    do_twice(func, arg)

do_four(print_twice, "spam")