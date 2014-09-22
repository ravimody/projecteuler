problem 38
What is the largest 1 to 9 pandigital 9-digit number that can be formed as the concatenated product of an integer with (1,2, ... , n) where n > 1?


max_n = 98765   # you don't need to check more than this


max_pandigital = 0
for i in range(1,max_n+1):
   pandigital_string = ''
   for j in range(1,10):
      pandigital_string = pandigital_string + str(i * j) 
      pandigital = int(pandigital_string)
      if pandigital > max_pandigital and is_num_pandigital(pandigital):
         max_pandigital = pandigital

print(max_pandigital)
# 932718654

def is_num_pandigital(num):
   return sorted(list(str(num))) == ['1','2','3','4','5','6','7','8','9']   


