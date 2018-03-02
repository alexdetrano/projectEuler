#!/usr/bin/python

n = 1000
candidates = []
# pairs of numbers that add up to 1000
for a in range(1, n-3):
    for b in range(2, n-2):
        for c in range(3, n-3):
            if (a + b + c == 1000) and (a < b < c):
                candidates.append((a,b,c))
print(len(candidates))

for triplet in candidates:
    if (triplet[0]**2 + triplet[1]**2 == triplet[2]**2):
        print(triplet[0] * triplet[1] * triplet[2])


