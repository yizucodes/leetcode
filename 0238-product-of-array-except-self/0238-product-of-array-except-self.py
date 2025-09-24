class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        res = [1] * len(nums)
        
        prefix = 1

        for i in range(len(nums)):
            res[i] = prefix
            prefix = nums[i] * prefix

        suffix = 1 
        for i in range(len(nums) - 1, -1, -1):
            res[i] = suffix * res[i]
            suffix = nums[i] * suffix

        return res

        