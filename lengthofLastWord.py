""" Given a string s consists of upper/lower-case alphabets and empty space characters ' ', return the length of last word in the string.

If the last word does not exist, return 0.

"""
class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        str = s.rstrip()
       # str = str.lstrip()
        str_list = str.split(' ')
        print str_list
        if(len(str_list) == 0):
            return 0
        return len(str_list[-1])
