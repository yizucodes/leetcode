class Solution:
    def climbStairs(self, n: int) -> int:

        # dp array
        dp = [-1] * (n + 1)
        
        # recursion
        def climb(steps):
            # base case is less than or equal to 1
            if steps <= 1:
                return 1
            # check if value computed in dp array return computed value if computed
            if dp[steps] != -1: 
                return dp[steps]
            dp[steps] = climb(steps - 1) + climb(steps - 2)
            return dp[steps]

        res = climb(n)
        return res

