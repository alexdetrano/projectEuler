#!/usr/bin/env python3
'''
Problem 29
==========


   Consider all integer combinations of a^b for 2 ≤ a ≤ 5 and 2 ≤ b ≤ 5:

     2^2=4, 2^3=8, 2^4=16, 2^5=32
     3^2=9, 3^3=27, 3^4=81, 3^5=243
     4^2=16, 4^3=64, 4^4=256, 4^5=1024
     5^2=25, 5^3=125, 5^4=625, 5^5=3125

   If they are then placed in numerical order, with any repeats removed, we
   get the following sequence of 15 distinct terms:

        4, 8, 9, 16, 25, 27, 32, 64, 81, 125, 243, 256, 625, 1024, 3125

   How many distinct terms are in the sequence generated by a^b for 2 ≤ a ≤
   100 and 2 ≤ b ≤ 100?


   Answer: 6f0ca67289d79eb35d19decbc0a08453

'''

# can probably do some optimization since we know we will get repeats
# eg 2^4 = 16 is the same as 4^2
#    2^6 = 64                4^3 
# so we can skip calculating some early terms for larger bases
min_a = 2
max_a = 100
min_b = 2
max_b = 100
terms = []
for a in range(min_a, max_a + 1):
    for b in range(min_b, max_b + 1):
        n = a**b
        if n not in terms:
            terms.append(n)
print(len(sorted(terms)),end='')
