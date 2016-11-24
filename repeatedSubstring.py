"""Given a non-empty string check if it can be constructed by taking a substring of it and appending multiple copies of the substring together. You may assume the given string consists of lowercase English letters only and its length will not exceed 10000.

Example 1:
Input: "abab"

Output: True

Explanation: It's the substring "ab" twice.
Example 2:
Input: "aba"

Output: False
Example 3:
Input: "abcabcabcabc"

Output: True

Explanation: It's the substring "abc" four times. (And the substring "abcabc" twice.)"""
class Solution(object):
    def repeatedSubstringPattern1(self, str):
        """
        :type str: str
        :rtype: bool
        """
        i = 0
        j = 1
        start = 0
        end = 1
        size = len(str)
        for j in range(1, size/2 + 1):
            i = start
            k = j
            while(k < size):
                if(str[i] == str[k]):
                    i = i + 1
                    k = k + 1
                    continue
                else:
                    break
            if(k == size):
                return True
                
        return False
    
    def repeatedSubstringPattern(self, str):
        size = len(str)
        for j in range(1, size/2 + 1):
            if(size % j):
                continue
            if(str[:j] * (size / j) == str):
                return True
        return False
