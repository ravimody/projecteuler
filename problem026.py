# Find the value of d < 1000 for which 1/d contains the longest recurring cycle in its decimal fraction part.

max_range = 1000
max_cycle_count = 0
max_cycle = 0

for i in range(2,max_range):
   cycle_count = division(1,i)
   if cycle_count > max_cycle_count:
      max_cycle_count = cycle_count
      max_cycle = i

print max_cycle, max_cycle_count
# 983 982

# implement long division, keeping track of the dividend. when it repeats, we know we found a cycle
def division(dividend, divisor):

   dividend_history= {}
   current_digit = 0

   while dividend > 0:
      while dividend < divisor:
         dividend *= 10
         current_digit += 1
         
      quotient = dividend / divisor

      dividend = dividend - (divisor * quotient)
      dividend *= 10
         
      if dividend_history.has_key(dividend):
         return current_digit - dividend_history[dividend]
   
      dividend_history[dividend] = current_digit
      current_digit += 1

   return current_digit  
   
   