class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        
        target = tickets[k]
        count_sec = 0

        for i,t in enumerate(tickets):
            if i <= k:
                count_sec += min(t,target)
            else:
                count_sec += min(t,target-1)

        return count_sec


