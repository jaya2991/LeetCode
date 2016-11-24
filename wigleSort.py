"""Given an unsorted array nums, reorder it such that nums[0] < nums[1] > nums[2] < nums[3]....

Example:
(1) Given nums = [1, 5, 1, 1, 6, 4], one possible answer is [1, 4, 1, 5, 1, 6]. 
(2) Given nums = [1, 3, 2, 2, 3, 1], one possible answer is [2, 3, 1, 3, 1, 2].

Note:
You may assume all input has valid answer.

Follow Up:
Can you do it in O(n) time and/or in-place with O(1) extra space?
"""
class Solution(object):
    def swap(self, nums, i, j):
        temp = nums[i]
        nums[i] = nums[j]
        nums[j] = temp
        
    def wiggleSort1(self, nums):
        i = 1
        while(i < len(nums)):
            if((i%2 == 0 and nums[i] > nums[i-1]) or (i%2 == 1 and nums[i] < nums[i-1])):
                self.swap(nums, i, i - 1)
                    
            i = i + 1
    def wiggleSort(self, nums):
        temp = sorted(nums)
        n = len(nums)
        if(n % 2 == 0):
            i, j = n/2 - 1, n - 1
        else:
            i, j = n/2, n - 1
        for k in range(n):
            if( k % 2 == 0):
               
                nums[k] = temp[i]
                i = i - 1
                
            else:
                
                nums[k] = temp[j]
                j = j - 1
        
