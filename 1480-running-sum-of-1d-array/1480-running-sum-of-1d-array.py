class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        currSum = 0
        res = []
        for num in nums:
            currSum += num
            res.append(currSum)
        return res