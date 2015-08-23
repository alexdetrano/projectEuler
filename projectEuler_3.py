__author__ = 'alexd'
from math import sqrt
import time
# Largest prime factor
# Problem 3
#
# The prime factors of 13195 are 5, 7, 13 and 29.
#
# What is the largest prime factor of the number 600851475143 ?


def isEven(n):
    if n % 2 == 0:
        return True
    else:
        return False

def isMult5(n):
    if n % 5 == 0:
        return True
    else:
        return False


def isPrime(n):
    if n <= 1:
        return False
    elif n % 2 == 0 and n > 2:
        return False
    for i in range(3, int(sqrt(n)) + 1, 2):
        if n % i == 0:
            return False
    return True

start_time = time.time()
n = 600851475143

print('start : n = {}'.format(n))
# divide the number down by 2
while n % 2 == 0:
    n /= 2
    largest_prime = 2
print('div2 :  n = {}'.format(n))

# now we can divide the number down even further by dividing down the odds
i = 3

while n != 1:
    while n % i == 0:
        n /= i
        largest_prime = i
    i += 2  # 3, 5, 7...
print('div3 :  n = {}'.format(n))
print('largest prime = {}'.format(largest_prime))
elapsed_time = time.time() - start_time
print('elapsed time: {:.2f}m {:.4f}s'.format(elapsed_time % 60, elapsed_time))
# primes = []
# for i in range(2, int(n/2) + 1):
#     (q, r) = divmod(n, i)
#     if r == 0:
#         print(q)

# print('max prime factor = ', max(primes))


# primes = []
# for i in range(2, int(n/2) + 1):
#     if n % i == 0:  # does i divide n?
#         if not isEven(i) or not isMult5(i):  # don't bother
#             print(i)
#             if isPrime(i):
#                 primes.append(i)
# print('max prime factor = ', max(primes))
