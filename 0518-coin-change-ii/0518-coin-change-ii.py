class Solution:
    def change(self, amount: int, coins: List[int]) -> int:

        memo = {}
      

        # n is amount, try to find num way to make amount n
        def dp(n, coinIndex):
            
            key = (n, coinIndex)
            # base cases
            # 1 way with no coinse to make 0
            if n == 0:
                return 1

            if n < 0:
                return 0

            if coinIndex >= len(coins):
                return 0
            
            if key in memo:
                return memo[key]

            # recurrence
            # try each coin in coins array to make sum to amount

            use = dp(n - coins[coinIndex], coinIndex)
                
            # Choice 2: Skip current coin (move to next coin)
            skip = dp(n, coinIndex + 1)

            memo[key] = use + skip

            return use + skip
        

        return dp(amount, 0)