"""Implement atoi to convert a string to an integer.

Hint: Carefully consider all possible input cases. If you want a challenge, please do not see below and ask yourself what are the possible input cases.

Notes: It is intended for this problem to be specified vaguely (ie, no given input specs). You are responsible to gather all the input requirements up front.
"""
class Solution(object):
    def isNum(self, s):
        if(s >= '0' and s <= '9'):
            return True
        return False
        
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        if(str == ""):
            return 0
            
        a = 1
        n = 0
        num = 0
        sign = 1
        str = str.strip()
        if(str[n] == '+'):
            sign = 1
            n = n + 1
        elif(str[n] == '-'):
            sign = -1
            n = n + 1
        while(n < len(str)):
            if(self.isNum(str[n])):
                num = num*10 + ord(str[n]) - 48
                n = n + 1
                print num, n
            else:
                if(sign*num > (2 ** 31 -1)):
                    return (2 ** 31 - 1)
                elif(sign*num < ((-2) ** 31)):
                    return ((-2) ** 31)
                return sign*num
        if(sign*num > (2 ** 31 -1)):
            return (2 ** 31 - 1)
        elif(sign*num < ((-2) ** 31)):
            return ((-2) ** 31)
        return sign*num
            
           
            
            
        
