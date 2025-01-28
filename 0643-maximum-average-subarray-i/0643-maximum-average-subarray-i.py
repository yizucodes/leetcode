class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        if k > len(nums):
            return None
        
        # length is 1 and k is 1 return nums[0]
        if len(nums) == 1 and k == 1:
            return nums[0]
        
        currSum = None
        currAvg = None
        maxAvg = float('-inf')
        window = nums[:k]

        for left in range(len(nums) - k + 1):
            right = left + k
            if currSum is None:
                currSum = sum(window)
            else:
                currSum = currSum - nums[left - 1]
                currSum = currSum + nums[right - 1]
            
            currAvg = currSum / k
            maxAvg = max(maxAvg, currAvg)
        
        return maxAvg   

            


