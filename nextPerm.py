"""Implement next permutation, which rearranges numbers into the lexicographically next greater permutation of numbers.

If such arrangement is not possible, it must rearrange it as the lowest possible order (ie, sorted in ascending order).

The replacement must be in-place, do not allocate extra memory.

Here are some examples. Inputs are in the left-hand column and its corresponding outputs are in the right-hand column.
1,2,3 → 1,3,2
3,2,1 → 1,2,3
1,1,5 → 1,5,1
"""
import sys
class Solution(object):
    def swap(self, nums, i, j):
        temp = nums[i]
        nums[i] = nums[j]
        nums[j] = temp
        
    def reverse_list(self, nums, i, j):
        if(i > j):
            return nums
        while(i <= j):
            self.swap(nums, i, j)
            i = i + 1
            j = j - 1
        return nums
        
    def findNextMin(self, nums, j):
        mindiff = sys.maxint
        minind = 0
        i = j + 1
        while(i < len(nums)):
            if(nums[i] - nums[j] <= mindiff and nums[i] - nums[j] > 0):
                mindiff = nums[i] - nums[j]
                minind = i
            i = i + 1
        return minind
        
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        j = n - 1
        if(n == 1):
            return
        if(n == 2):
            if(nums[0] < nums[1]):
                self.swap(nums, 0, 1)
            else:
                self.reverse_list(nums, 0, n-1)
            return
        
        while( j >= 0):
            if(nums[j] > nums[j-1]):
                j = j - 1
                break
            j = j - 1
        if(j == -1):
            self.reverse_list(nums, 0, n-1)
            return 
        i = self.findNextMin(nums, j)
        self.swap(nums, i, j)
        self.reverse_list(nums, j + 1, n-1)
        
            
        
