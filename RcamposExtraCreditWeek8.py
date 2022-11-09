# -*- coding: utf-8 -*-
"""
Created on Wed Nov  2 08:15:47 2022

@author: ronal
"""

# Python3 code to find largest prime

import math

# A method to find largest prime factor
def maximumPrimeFactors (n):

maxPrime = -1
while n % 2 == 0:
maxPrime = 2
n /= 2
for i in range(3, int(math.sqrt(n)) + 1, 2):
while n % i == 0:
maxPrime = i
print(maxPrime,end=" ")
n = n / i

if n > 2:
maxPrime = n

return int(maxPrime)

n1 = 13195
r1 = maximumPrimeFactors(n1)
print()
n2 = 600851475143
r2 = maximumPrimeFactors(n)

print("\nLargest prime factor of {} is {}".format(n1,r1))
print("Largest prime factor of {} is {}".format(n2,r2))