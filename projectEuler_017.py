#!/usr/bin/env python
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
n = 121
sum = 0
for i in range(n, n + 1):
    if i < 20:
        sum += digits[i]
    else:
        _i = i  # make a local copy
        p = 0
        while _i:
            p += 1
            d = _i % 10
            print(_i, d, p)
            _i = _i // 10
print(sum)
