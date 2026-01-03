class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        if len(nums) == 1 and k == 1:
            return nums[0]
        
        # winSum
        winSum = sum(nums[:k])
        # maxSum
        maxSum = winSum

        # traverse array from k to len(nums)
        for r in range(k, len(nums)):
            # calc winSum by subracting the leftmost element, add the rightmost element
            winSum = winSum - nums[r - k] + nums[r]

            # maxSum calc
            maxSum = max(maxSum, winSum)

        return maxSum / k