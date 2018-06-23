#!/usr/bin/env python
"""Challenge 17"""
import pdb
from pprint import pprint 

digits = {
    0: 0,
    1: len('one'),
    2: len('two'),
    3: len('three'),
    4: len('four'),
    5: len('five'),
    6: len('six'),
    7: len('seven'),
    8: len('eight'),
    9: len('nine'),
    10: len('ten'),
    11: len('eleven'),
    12: len('twelve'),
    13: len('thirteen'),
    14: len('fourteen'),
    15: len('fifteen'),
    16: len('sixteen'),
    17: len('seventeen'),
    18: len('eighteen'),
    19: len('nineteen'),
    20: len('twenty'),
    30: len('thirty'),
    40: len('forty'),
    50: len('fifty'),
    60: len('sixty'),
    70: len('seventy'),
    80: len('eighty'),
    90: len('ninety'),
}
n = 1000
sum = 0
s = {}
for i in range(1, n+1):
    sum_old = sum
    # handle last two digits
    last_two_digits = i % 100
    if last_two_digits in digits:
        sum += digits[last_two_digits]
    else:
        tens = last_two_digits // 10 * 10
        ones = last_two_digits % 10
        sum += digits[tens] + digits[ones]

    # take into account word 'and' in large numbers
    # don't count multiples of 100 since no 'and' in those numbers
    # eg 215 = two hundred and fifteen
    # eg 200 = two hundred
    if i > 100 and i % 100 != 0:
        sum += len('and')

    # we handled last two digits so let's deal with remaining
    if i >= 100 and i < 1000:
        sum += digits[i // 100]
        sum += len('hundred')
    elif i == 1000:
        sum += digits[i // 1000]
        sum += len('thousand')
    sum_new = sum
    # group together all numbers  by len for debug
    try:
        s[sum_new-sum_old].append(i)
    except KeyError:
        s[sum_new-sum_old] = [i]
    print(f'i={i:4}, len={sum_new-sum_old}')
#pprint(s)
print(sum)

