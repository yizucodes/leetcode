class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        # binary search
        l = 0
        r = len(nums) - 1

        while l <= r:
            m = (l + r) // 2

            if nums[m] == target:
                return m

            # left is sorted
            if nums[l] <= nums[m]:
                # is target sorted in left range?
                if nums[l] <= target <= nums[m]:
                    r = m - 1
                else:
                    l = m + 1

            # right is sorted
            else:
                # target in the sorted right range?
                if nums[m] <= target <= nums[r]:
                    l = m + 1
                else:
                    r = m - 1

        return -1

        