class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        total = sum(nums)
        left = 0

        for i in range(len(nums)):
            if left == total - left - nums[i]:
                return i
            left = left + nums[i]
            right = total - left - nums[i]

            
        return -1