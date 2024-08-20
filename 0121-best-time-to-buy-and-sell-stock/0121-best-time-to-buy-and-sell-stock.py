class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) == 1:
            return 0
        
        maxProfit = 0
        currPrice = prices[0]

        for i in range(1, len(prices)):
            tempProfit = prices[i] - currPrice
            
            if prices[i] < currPrice:
                currPrice = prices[i]

            # if greater then replace maxProfit with tempProfit
            if tempProfit > maxProfit:
                maxProfit = tempProfit

        return maxProfit
            
           


            




