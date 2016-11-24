"""Given a collection of numbers that might contain duplicates, return all possible unique permutations.

For example,
[1,1,2] have the following unique permutations:
[
  [1,1,2],
  [1,2,1],
  [2,1,1]
]
"""
class Solution(object):
    def swap(self, nums, i, j):
        nums[i], nums[j] = nums[j], nums[i]
        
    def permute_helper(self, nums, curr, perm, n):
        if(curr == n):
            perm.append(nums[:])
            return
        s = set([])
        for i in range(curr, n):
            if(nums[i] in s):
                continue
            s.add(nums[i])
            self.swap(nums, i, curr)
            self.permute_helper(nums, curr+1, perm, n)
            self.swap(nums, i, curr)
            
                
            
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        curr = 0
        perm = []
        n = len(nums)
        self.permute_helper(nums, curr, perm, n)
        
        return perm
