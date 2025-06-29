class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:

        memo = [-1] * (amount + 1)

        # What's the minimum number of coins needed to make amount n
        def dp(n):
            # base case:
            if n == 0:
                return 0
            # check
            if n < 0:
                return float('inf')
            
            if memo[n] != -1:
                return memo[n] 

            # Try each coin in coins to see which gives min total
            minCoins = float('inf')

            for coin in coins:
                res = dp(n - coin)
                # add 1 to count used coin
                minCoins = min(minCoins, 1 + res)
            
            memo[n] = minCoins

            return minCoins

        result = dp(amount)

        if result == float('inf'):
            return -1
        return result

