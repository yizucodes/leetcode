class Solution:
    def findMin(self, nums: List[int]) -> int:
        nums = sorted(nums)
        return nums[0]