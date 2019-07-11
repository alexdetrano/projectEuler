#!/usr/bin/env python3
'''
Problem 20
==========

 n! means n × (n − 1) × ... × 3 × 2 × 1

   For example, 10! = 10 × 9 × ... × 3 × 2 × 1 = 3628800,
   and the sum of the digits in the number 10! is 3 + 6 + 2 + 8 + 8 + 0 + 0 =
   27.

   Find the sum of the digits in the number 100!
'''

n = 100
i = 1
nfactorial = 1

while i <= n:
    nfactorial = i * nfactorial
    i += 1

print(sum([int(x) for x in str(nfactorial)]), end='')

