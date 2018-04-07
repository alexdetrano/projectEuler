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
    Return True if a number is prime
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


def get_primes(start):
    """
    Generate a list of prime numbers starting at n
    """
    while True:
        if is_prime(start):
            yield(start)
        start += 1


def get_triangle_numbers():
    """
    Generate a list of triangle numbers

    Sequence of triangle numbers can be generated by adding
    the natural numbers. Eg: 1,3,6,10,15...
    """
    i = 0
    sum = 0
    while True:
       i += 1
       sum += i
       yield(sum)



        
    

