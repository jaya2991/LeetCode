class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        n = len(nums)
        # result = []
        # for i in range(n-1):
        #     for j in range(i+1, n):
        #         if nums[i] + nums[j] == target:
        #             return [i, j]
        nums_dict = {}

        for i, num in enumerate(nums):
            remaining = target - num
            if remaining in nums_dict:
                return [i, nums_dict[remaining]]
            nums_dict[num] = i
