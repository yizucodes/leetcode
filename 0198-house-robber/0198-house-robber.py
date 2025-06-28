class Solution:
    def rob(self, nums: List[int]) -> int:
        # dp array
        dp = [-1] * (len(nums) + 1)

        # index of house
        def robbing(i):
            # base case i >= len(nums)
            if i >= len(nums):
                return 0

            # if value in dp array --> return that value
            if dp[i] != -1:
                return dp[i]

            # take
            take = nums[i] + robbing(i + 2)

            # not take
            notTake = robbing(i + 1)

            res = max(take, notTake)
            # store values in dp array
            dp[i] = res 

            return res

        return robbing(0)


        









