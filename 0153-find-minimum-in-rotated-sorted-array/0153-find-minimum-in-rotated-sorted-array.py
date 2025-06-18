class Solution:
    def findMin(self, nums: List[int]) -> int:
        # binary search

        l = 0
        r = len(nums) - 1

        while l <= r:
            m = (l + r) // 2

            # go right if m > nums[r]
            if nums[m] > nums[r]:
                l = m + 1
            else:
                r = m
        
        return nums[l]

        
