"""Given a string, find the length of the longest substring without repeating characters.

Examples:

Given "abcabcbb", the answer is "abc", which the length is 3.

Given "bbbbb", the answer is "b", with the length of 1.

Given "pwwkew", the answer is "wke", with the length of 3. Note that the answer must be a substring, "pwke" is a subsequence and not a substring.

"""

class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        visited = [-1] * 256
        currLen = 0
        maxLen = 0
        
        for l in range(len(s)):
            prevInd = visited[ord(s[l]) - 97]
            
            if(prevInd == -1 or l - currLen > prevInd):
                currLen = currLen + 1
                
            else:
                if(currLen > maxLen):
                    maxLen = currLen
                currLen = l - prevInd
            visited[ord(s[l]) - 97] = l
        if(currLen > maxLen):
            maxLen = currLen
            
        return maxLen
