__author__ = 'alexd'


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