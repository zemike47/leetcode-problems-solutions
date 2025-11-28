from collections import deque

class Solution:
    def deckRevealedIncreasing(self, deck: list[int]) -> list[int]:
        deck.sort(reverse=True)
        dq = deque()

        for card in deck:
            if dq:
                dq.appendleft(dq.pop())
            dq.appendleft(card)
        
        return list(dq)
     
