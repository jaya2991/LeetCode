"""Write a function to find the longest common prefix string amongst an array of strings.

"""
class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if(len(strs) == 0 or (len(strs) == 1 and strs[0] == "")):
            return ""
        
        prefix = strs[0]
        for i in range(len(strs)):
            while(strs[i].find(prefix, 0, len(strs[i])) != 0):
                prefix = prefix[:len(prefix) - 1]
                if(len(prefix) == 0):
                    return ""
        return prefix
