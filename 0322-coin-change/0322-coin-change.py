class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # create a memo ar
        memo = [-1] * (amount + 1)

        # dp(n) # n is the amount and you are trying to minimize the number of coins to cover that amount by trying each coin in coins array
        def dp(n):

            # base case
            # n == 0 return 0
            if n == 0:
                return 0

            # n < 0 return infinity
            if n < 0:
                return float('inf')

            # check if memoized value is there
            if memo[n] != -1:
                return memo[n]

            minCoin = float('inf')

            # recurrence
            for coin in coins:
                minCoin = min(minCoin, 1 + dp(n - coin))
            
            # assign value from recurrence
            memo[n] = minCoin

            return minCoin

        mini = dp(amount)

        if mini == float('inf'):
            return -1

        return mini

