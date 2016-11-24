"""Given a collection of distinct numbers, return all possible permutations.

For example,
[1,2,3] have the following permutations:
[
  [1,2,3],
  [1,3,2],
  [2,1,3],
  [2,3,1],
  [3,1,2],
  [3,2,1]
]
"""
class Solution(object):
    def swap(self, nums, i, j):
        nums[i], nums[j] = nums[j], nums[i]
        
    def permute_helper(self, nums, curr, perm, n):
        if(curr == n):
            
            perm.append(nums[:])
            return
        for i in range(curr, n):
            self.swap(nums, i, curr)
            self.permute_helper(nums, curr+1, perm, n)
            self.swap(nums, i, curr)
            
                
            
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        curr = 0
        perm = []
        n = len(nums)
        self.permute_helper(nums, curr, perm, n)
        
        return perm
