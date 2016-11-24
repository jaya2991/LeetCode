"""Implement pow(x, n)."""
class Solution(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        if(n == 0):
            return 1
        if(n < 0):
            return 1 / self.myPow(x, -n)
        y = self.myPow(x, n>>1)
        if n & 1:
            return y * y * x
        else:
            return y * y
        
