__author__ = 'alexd'
from common import *
from functools import reduce

# Smallest multiple
# Problem 5
#
# 2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
#
# What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

def lcmm(*args):
    """
    Return lcm of args.
    See http://stackoverflow.com/questions/147515/least-common-multiple-for-3-or-more-numbers
    :param args:
    :return:
    """
    return reduce(lcm, args)
print(lcmm(*range(1,21)))

