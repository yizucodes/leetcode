class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # if amount > all coins --> -1

        # if amount 0 return 0
        memo = [-1] * (amount + 1)

        # Think: "To make amount 7, I could use any of my coins as the last coin. Let me try each one and see which gives the minimum total."

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
                minCoins = min(minCoins, 1 + res)
            
            memo[n] = minCoins

            return minCoins

        result = dp(amount)

        if result == float('inf'):
            return -1
        return result

                
