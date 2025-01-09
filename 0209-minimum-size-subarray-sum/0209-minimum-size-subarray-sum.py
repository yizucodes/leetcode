class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:

        left = 0
        min_length = float('inf')
        currSum = 0

        for right in range(len(nums)):
            currSum += nums[right]
            # shrink window
            while currSum >= target:
                min_length = min(min_length, right - left + 1)
                currSum -= nums[left]
                left += 1

        
        if min_length == float('inf'):
            return 0
            
        return min_length

