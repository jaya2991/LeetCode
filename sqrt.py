""" Implement int sqrt(int x).

Compute and return the square root of x."""
class Solution(object):
    def mySqrt(self, x):
       if(x == 0 or x == 1):
           return x
       start = 0
       end = x
       
       while(start <= end):
           mid = (start + end)/2
           if(mid*mid == x):
               return mid
           if(mid*mid < x):
               start = mid + 1
               ans = mid
           else:
               end = mid - 1
       return ans
