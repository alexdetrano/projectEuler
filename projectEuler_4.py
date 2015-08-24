__author__ = 'alexd'
# largest palindromic number from product of two 2-digit numbers is 9009 (91 x 99)
# find largest palindrome made from the product of two 3-digit numbers

def isPalindrome(n):
    """
    Check if a number is a palindrome number.

    This is the brute-force (naive) method, since we always compare the entire string.
    An improvement would be to check the first digit vs the last, and if not equal, immediately return false.
    :param n: integer to check
    :return: True if palindrome, False if not palindrome.
    """
    if str(n) == str(n)[::-1]:
        return True
    else:
        return False

max_palindrome = 0
for x in range(100, 999 + 1):
    for y in range(100, 999 + 1):
        prod_xy = x * y
        if isPalindrome(prod_xy):
            if prod_xy > max_palindrome:
                max_palindrome = prod_xy
print(max_palindrome)