class Solution:
    def findMin(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        
        # binary search
        l = 0
        r = len(nums) - 1

        while l < r:
            m = (l + r) // 2

            # num[m] > nums[right] --> go right
            if nums[m] > nums[r]:
                l = m + 1

            # go left
            else:
                r = m

        return nums[l]