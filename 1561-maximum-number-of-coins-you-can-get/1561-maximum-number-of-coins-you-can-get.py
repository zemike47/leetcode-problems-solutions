class Solution:
    def maxCoins(self, piles: list[int]) -> int:
        piles.sort()
        i = len(piles) - 2
        no_coins = len(piles) // 3
        coins = 0
        rounds = 0

        while rounds < no_coins:
            
            coins += piles[i]

            i -= 2
            rounds += 1
        
        return coins


            

