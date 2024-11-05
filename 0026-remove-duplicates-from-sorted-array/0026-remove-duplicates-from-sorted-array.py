class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 1
        
        left = 0
        right = 1
        
        while right < len(nums):
            if nums[left] == nums[right]:
                nums.pop(right)
            else:
                left += 1
                right += 1

        return len(nums)
        
        
        