class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:

        memo = [-1] * len(cost)
        
        # index
        def dp(i):

            # base case
            if i >= len(cost):
                return 0
                
            # check if value exists to avoid recomputing subproblem
            if memo[i] != -1:
                return memo[i]

            take = cost[i] + min(dp(i + 1), dp(i + 2))

            # add res to memo array
            memo[i] = take

            return take

        resZero = dp(0)
        resOne = dp(1)

        return min(resZero, resOne)