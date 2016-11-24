"""Implement regular expression matching with support for '.' and '*'.

'.' Matches any single character.
'*' Matches zero or more of the preceding element.

The matching should cover the entire input string (not partial).

The function prototype should be:
bool isMatch(const char *s, const char *p)

Some examples:
isMatch("aa","a") → false
isMatch("aa","aa") → true
isMatch("aaa","aa") → false
isMatch("aa", "a*") → true
isMatch("aa", ".*") → true
isMatch("ab", ".*") → true
isMatch("aab", "c*a*b") → true
"""
class Solution(object):
    def isMatch(self, s, p):
        len_p = len(p)
        len_s = len(s)
        
        if len_p == 0 and len_s == 0:
            return True
        if len_p == 0 and len_s != 0:
            return False
        if len_s == 0:
            if len_p == 2 and p[1] == '*':
                return True
            else:
                return False
        if len_p > 1 and p[1] == '*':
            ret = self.isMatch(s, p[2:])
            if (s[0] == p[0] or p[0] == '.'):
                ret = ret or self.isMatch(s[1:], p[2:]) or self.isMatch(s[1:], p)
            return ret
        if s[0] == p[0] or p[0] == '.':
            return self.isMatch(s[1:],p[1:])
        return False
        
