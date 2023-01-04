class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0:
            return False
        num = x
        rem = None
        rev_num = 0
        
        while num:
            rem = num % 10
            rev_num = rev_num * 10 + rem
            num = num//10
        if x == rev_num:
            return True 
        return False

