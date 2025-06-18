class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if len(nums) == 1:
            if target == nums[0]:
                return 0
            else:
                return -1
            
        def b_search(nums, target, left, right):

            # base case
            if left > right:
                return -1
            
            m = (left + right) // 2

            # when you find the number
            if nums[m] == target:
                return m
            
            # go right if target >= m
            if target > nums[m]:
                return b_search(nums, target, m + 1, right)
            else:
                return b_search(nums, target, left, m - 1)

        
        return b_search(nums, target, 0, len(nums) - 1)

        