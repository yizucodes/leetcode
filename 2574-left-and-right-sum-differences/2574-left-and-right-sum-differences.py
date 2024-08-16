class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:

        # For 1 number in nums return [0]
        if len(nums) == 0:
            return [0]
        
        length = len(nums)
        # Find leftSum

        leftSum = [0] * length
        prefix = 0
        for i in range(1, length):
            prefix = prefix + nums[i - 1]
            leftSum[i] = prefix
            

        # Find rightSum
        suffix = 0
        rightSum = [0] * length
        for j in range(length - 2, -1, -1):
            suffix = suffix + nums[j + 1]
            rightSum[j] = suffix
        
        # Find difference between leftSum and rightSum, take absolute value of difference
        res = []
    
        for ind in range(length):
            res.append(abs(leftSum[ind] - rightSum[ind]))
        
        return res



        