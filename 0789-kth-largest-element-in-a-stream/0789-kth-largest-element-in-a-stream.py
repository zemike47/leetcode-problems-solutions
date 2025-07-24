import heapq

class KthLargest:

    def __init__(self, k: int, nums: list[int]):
        self.k = k
        self.min_heap = nums
        heapq.heapify(self.min_heap)  # Turn nums into a min-heap
        
        # Only keep k elements in the heap
        while len(self.min_heap) > k:
            heapq.heappop(self.min_heap)
        
    def add(self, val: int) -> int:
        heapq.heappush(self.min_heap, val)  # Add new score
        
        if len(self.min_heap) > self.k:
            heapq.heappop(self.min_heap)  # Maintain size k
        
        return self.min_heap[0]  # kth largest is the smallest in heap
