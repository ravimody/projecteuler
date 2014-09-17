# What is the value of the first triangle number to have over five hundred divisors?


# nth triangle number m = n * (n+1) / 2
# steps:
# 1 - collect the prime factors of n and n-1 and combine them
# 2 - subtract one from the 2 column to divide by 2
# 3 - take the product of (the number of prime factors in each + 1). this is the number of prime factors for m


from math import sqrt

max_search = 1000000

primes = [2]
prev_prime_factorization = {2:1}
for n in range(3,max_search):
   #step 1
   prime_factorization = factorization(n, primes)
   combined_factorization = combine_factorizations(prime_factorization, prev_prime_factorization)
   prev_prime_factorization = prime_factorization
   
   #step 2
   combined_factorization[2] = combined_factorization.get(2,1) - 1 
   
   #step 3
   num_factors = reduce(lambda x, y: x * y, map(lambda x: x+1, combined_factorization.values()))
   if num_factors > 500: 
      print n * (n - 1) / 2, num_factors
      break
   
 
def factorization(num, primes):
   prime_dict = {} 
   for divisor in primes:
      if (divisor > num): 
         break
      while (num % divisor == 0):
         prime_dict[divisor] = prime_dict.get(divisor, 0) + 1
         num = num / divisor
         continue
   if prime_dict == {}:
      prime_dict[num] = prime_dict.get(num, 0) + 1      
      primes.append(num)
   return prime_dict


def combine_factorizations(x,y):
   return { k: x.get(k, 0) + y.get(k, 0) for k in set(x) | set(y) }





