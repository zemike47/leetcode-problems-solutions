class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxProfit = 0 
        lowday = prices[0]

        for i in range(len(prices)):
            if prices[i] < lowday:
                lowday = prices[i]
            
            maxProfit = max(maxProfit,prices[i] - lowday)
        
        return maxProfit


        
       
