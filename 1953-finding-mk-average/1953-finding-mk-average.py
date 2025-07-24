from collections import deque
from sortedcontainers import SortedList

class MKAverage:

    def __init__(self, m: int, k: int):
        self.m = m
        self.k = k
        self.stream = deque()  # keep the last m elements
        self.low = SortedList()  # k smallest
        self.mid = SortedList()  # m - 2k middle values
        self.high = SortedList()  # k largest
        self.mid_sum = 0  # sum of mid values only

    def addElement(self, num: int) -> None:
        self.stream.append(num)

        # Step 1: Insert num into one of the three sets
        if not self.low or num <= self.low[-1]:
            self.low.add(num)
        elif not self.high or num >= self.high[0]:
            self.high.add(num)
        else:
            self.mid.add(num)
            self.mid_sum += num

        # Step 2: Remove oldest element if stream exceeds size m
        if len(self.stream) > self.m:
            old = self.stream.popleft()
            if old in self.low:
                self.low.remove(old)
            elif old in self.high:
                self.high.remove(old)
            else:
                self.mid.remove(old)
                self.mid_sum -= old

        # Step 3: Rebalance so that each set has the correct size
        while len(self.low) > self.k:
            val = self.low.pop()
            self.mid.add(val)
            self.mid_sum += val

        while len(self.high) > self.k:
            val = self.high.pop(0)
            self.mid.add(val)
            self.mid_sum += val

        while len(self.low) < self.k and self.mid:
            val = self.mid.pop(0)
            self.mid_sum -= val
            self.low.add(val)

        while len(self.high) < self.k and self.mid:
            val = self.mid.pop()
            self.mid_sum -= val
            self.high.add(val)

    def calculateMKAverage(self) -> int:
        if len(self.stream) < self.m:
            return -1
        return self.mid_sum // (self.m - 2 * self.k)
