class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        # find total

        total = sum(nums)
        left = 0

        for i in range(len(nums)):
            if left == total - left - nums[i]:
                return i
            left = left + nums[i]
            right = total - left - nums[i]

        # check if left and right sum are the same


        # non-existent

        return -1
