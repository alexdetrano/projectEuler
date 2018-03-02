__author__ = 'alexd'
from math import sqrt

def gcd(a,b):
    """
    Calculate the gcd using Euclid's algorithm
    :param a: integer
    :param b: integer
    :return: gcd integer
    """
    while b:  # while b is not 0
        print(a,b)
        a, b = b, a % b
    return a


def lcm(a,b):
    """
    Calculate the least common multiple.
    :param a: int
    :param b: int
    :return: lcm as an int
    """
    return abs(a*b) // gcd(a, b)


def is_prime(n):
    """
    Return True if a number is priome
    """
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
