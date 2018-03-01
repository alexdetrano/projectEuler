#!/bin/python
from math import sqrt
import sys

def is_prime(n):
    if n is None:
        # should really raise exception
        return False

    # negative numbers, zero, and 1 are not prime
    if n < 2:
        return False

    # only even prime is 2
    if n == 2:
        return True

    # no even number can be prime except 2
    if (n % 2) == 0:
        return False

    for i in range(3, int(sqrt(n)) + 1, 2):
        if n % i == 0:
            return False
    return True

n = 10001

i = 3 # we always include 2 to make incrementing odd numbers easier in the loop
p = 1 # we cheat and always count 2
# don't stop until we've found the nth prime
while True:
    # print(i)
    # keep track of how many primes we've found
    if is_prime(i):
        p += 1
    # breaking condition means we've found the nth prime
    if p == n:
        break
    # only check odd numbers
    i += 2
print(i)
