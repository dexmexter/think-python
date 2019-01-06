def any_lowercase1(s):
    for c in s:
        if c.islower():
            return True # returns True if first letter is lowercase
        else:
            return False # returns False if first letter is not lowercase

def any_lowercase2(s):
    for c in s:
        if "c".islower(): # This will always return the string 'True' b/c the letter 'c' is lowercase
            return 'True'
        else:
            return 'False'

def any_lowercase3(s):
    for c in s:
        flag = c.islower() # The flag will change with every letter and stay with the value of the last character
    return flag # only returns the flag for the final character

def any_lowercase4(s):
    flag = False
    for c in s:
        flag = flag or c.islower() # If c is uppercase, the flag changes to true and remains that way
    return flag

def any_lowercase5(s):
    for c in s:
        if not c.islower():
            return False # will return False if any letter is uppercase
    return True # will return True if every letter was lowercase 
