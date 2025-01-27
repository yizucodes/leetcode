class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        # Calculate first window sum
        currSum = sum(nums[:k])
        maxSum = currSum
        
        # Slide from left to right
        for i in range(len(nums) - k):
            # Remove leftmost element of current window
            currSum -= nums[i]
            # Add next element on the right
            currSum += nums[i + k]
            maxSum = max(maxSum, currSum)
            
        return maxSum / k