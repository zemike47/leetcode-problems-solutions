class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0

        min_stock = prices[0]

        for i in range(1,len(prices)):
            if prices[i] < min_stock:
                min_stock = prices[i]
            
            max_profit = max(max_profit,prices[i] - min_stock)
        
        return max_profit

            



        