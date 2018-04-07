#!/usr/bin/python

from common import is_prime

n = 2000000
sum = 2  # start sum at 2 so we can increment by 2
for i in range(3,n,2):
    if is_prime(i):
        sum += i
print(sum)
