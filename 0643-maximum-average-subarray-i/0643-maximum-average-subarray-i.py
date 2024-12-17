class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        # length 1 and k is 1
        if len(nums) == 1 and k == 1:
            return nums[0]

        # what to return if k is greater than len(nums)
        # return 0 for now
        if k > len(nums):
            return 0

        currentSum = 0

        # find current sum
        for i in range(k):
            currentSum += nums[i]

        maxSum = currentSum
        
        # slide window
        for i in range(k, len(nums)):
            currentSum += nums[i]
            currentSum -= nums[i-k]

            maxSum = max(maxSum, currentSum)

        return maxSum / k




