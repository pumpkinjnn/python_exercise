#For testing map, not using lower() 
from functools import reduce

DIGITS = {'0': 0, '1': 1, '2': 2, '3': 3, 
'4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '.': -1}

not_digit = 0;

def prod(L):
    return reduce(lambda x, y : x * y, L)

def str2float(s):
    nums = map(lambda x : DIGITS[x], s)
    def to_floate(total, cur):
        global not_digit
        if cur == -1:
            not_digit = 1
            return total
        if not_digit == 0:
            return 10*total + cur
        else:
            not_digit = not_digit * 10
            return total + cur/not_digit
    return reduce(to_floate, nums, 0.0)
