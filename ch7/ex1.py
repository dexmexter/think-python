import math

def mysqrt(a):
    x = a
    while True:
        y = (x + a/x) / 2
        if abs(y - x) < 0.000000000000000001:
            break
        x = y
    return x

def test_sqrt():
    
    titles = ['a', 'mysqrt(a)', 'math.sqrt(a)', 'diff']
    
    a_list = []
    mysqrt_list = []
    mathsqrt_list = []
    diff_list = []
    
    for i in range(1, 10):
        a_list.append(float(i))
        mysqrt_list.append(mysqrt(float(i)))
        mathsqrt_list.append(math.sqrt(i))

    for i in range(len(a_list)):
        diff_list.append(abs(mysqrt_list[i] - mathsqrt_list[i]))
        mysqrt_list[i] = round(mysqrt_list[i], 11)
        mathsqrt_list[i] = round(mathsqrt_list[i], 11)

    data = [titles] + list(zip(a_list, mysqrt_list, mathsqrt_list, diff_list))

    for i, d in enumerate(data):
        line = " ".join(str(x).ljust(14) for x in d)
        print(line)
        if i == 0:
            print('-' * len(line))

print(test_sqrt())