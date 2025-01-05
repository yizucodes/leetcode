class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        left = 0
        total = 0
        res = float('inf')

        for right in range(len(nums)):
            total += nums[right]
            while total >= target:
                lenCurrWindow = right - left + 1
                res = min(lenCurrWindow, res)
                total -= nums[left]
                left += 1
        
        if res == float('inf'):
            return 0
        
        return res
                