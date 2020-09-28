"""
Exercise 2

Read the documentation of the dictionary method setdefault and use it to write
a more concise version of invert_dict. Solution:
http://thinkpython2.com/code/invert_dict.py.
"""

def invert_dict(d):
    res = {}
    for key in d:
        res.setdefault(d[key], key)

    return res

test = { "cat": 'one', 'dog': 'two', 'fish': 'three'}

print(invert_dict(test))
