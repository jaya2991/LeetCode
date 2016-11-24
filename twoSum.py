"""Given an array of integers, return indices of the two numbers such that they add up to a specific target.

You may assume that each input would have exactly one solution.

Example:
Given nums = [2, 7, 11, 15], target = 9,

Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].
"""
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        nums_dict = {}
        nums_list = []
        for i in range(len(nums)):
            key = target - nums[i]
            if (nums_dict.has_key(key)):
                nums_list.append(nums_dict[key])
                nums_list.append(i)
            else:
                nums_dict[nums[i]] = i
        
        return nums_list
        
