class RecentCounter:

    def __init__(self):
        self.requests = []
        

    def ping(self, t: int) -> int:
        self.requests.append(t)

        initial = t - 3000
        
        count = 0

        for req in self.requests:
            if req >= initial and req <= t:
                count += 1
        
        return count




        


# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)