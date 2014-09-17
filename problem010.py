# problem 10: find the sum of all the primes below two million

from math import sqrt

n = 2000000

# start primes at 2 - we know it's prime, and now we can just concentrate on odd numbers
primes = [2]

# loop through all possible prime numbers 
for i in range(3,n,2):
   for j in primes:
      if (j > sqrt(i)): 
         primes.append(i)
         break
      if (i % j == 0):
         break
   
