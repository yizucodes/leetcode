class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        # if there is 1 num return nums


        # runningSum
        runningSum = nums[0]
        res = [nums[0]]

        # add runningSum for each element in array and append that to res array
        for i in range(1, len(nums)):
            runningSum += nums[i]
            res.append(runningSum)
        
        return res



        