class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:

        left = 0
        right = k

        runningSum = sum(nums[:k])
        maxAve = runningSum / k

        
        while right < len(nums):
            
            runningSum = runningSum - nums[left] + nums[right]

            # calculate the ave
            currAve = runningSum / k

            # take max btw current average and maxAve
            maxAve = max(currAve, maxAve)

            # move left and right pter by 1
            left += 1
            right += 1

        return maxAve