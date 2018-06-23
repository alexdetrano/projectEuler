#!/usr/bin/env python

#   Starting in the top left corner of a 2×2 grid, and only being able to move
#   to the right and down, there are exactly 6 routes to the bottom right
#   corner.
#
#   How many such routes are there through a 20×20 grid?

r = 2
c = 2
max_r = r - 1
max_c = c - 1
grid = [[0]* c for i in range(0,r)]
print(grid)

for i in range(0,r):
    for j in range(0,c):
        print(i,j)

