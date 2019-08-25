#!/usr/bin/env python3

#Problem 35
#==========
#
#
#   The number, 197, is called a circular prime because all rotations of the
#   digits: 197, 971, and 719, are themselves prime.
#
#   There are thirteen such primes below 100: 2, 3, 5, 7, 11, 13, 17, 31, 37,
#   71, 73, 79, and 97.
#
#   How many circular primes are there below one million?
#
#
#   Answer: b53b3a3d6ab90ce0268229151c9bde11

from common import is_prime

def is_circular_prime(x):
    # if initial number is not prime, bail out early
    if not is_prime(x):
        return False

    x = str(x)
    for i in range(1,len(x)):
        # right-half + left half
        final = x[i:] + x[0:i]
        if not is_prime(int(final)):
            return False
    return True


n = int(1000000)
cnt = 0
for i in range(1,n+1):
    if is_circular_prime(i):
        cnt += 1
print(cnt,end='')
