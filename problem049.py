# The arithmetic sequence, 1487, 4817, 8147, in which each of the terms increases by 3330, is unusual in two ways: (i) each of the three terms are prime, and, (ii) each of the 4-digit numbers are permutations of one another.
# There are no arithmetic sequences made up of three 1-, 2-, or 3-digit primes, exhibiting this property, but there is one other 4-digit increasing sequence.
# What 12-digit number do you form by concatenating the three terms in this sequence?


from math import sqrt


# reuse code from problem 10 - generate all primes up to 9999
n = 9999

primes = [2]

# loop through all possible prime numbers 
for i in range(3,n,2):
   for j in primes:
      if (j > sqrt(i)): 
         primes.append(i)
         break
      if (i % j == 0):
         break
   

four_digit_primes = [i for i in primes if i >= 1000]


for i in four_digit_primes:
   for j in four_digit_primes:
      if j > i: 
         if sorted(list(str(i))) == sorted(list(str(j))):
            k = j + (j - i)
            if k in four_digit_primes:
               if sorted(list(str(j))) == sorted(list(str(k))):
                  print i,j,k

#1487 4817 8147
#296962999629