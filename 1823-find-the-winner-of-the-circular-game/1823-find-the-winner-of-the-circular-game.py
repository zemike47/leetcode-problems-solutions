from collections import deque
class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        friends = []

        for i in range(1,n+1):
            friends.append(i)

        circle = deque(friends)

        while len(circle) > 1:
            rotation = k

            while rotation > 1:
                circle.append(circle.popleft())
                rotation -= 1
            
            circle.popleft()
        
        return circle[-1]
            


        
