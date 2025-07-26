class Solution:
    def canCompleteCircuit(self, gas: list[int], cost: list[int]) -> int:
            total_tank = 0
            curr_tank = 0
            start_index = 0

            for i in range(len(gas)):
                gain = gas[i] - cost[i]
                total_tank += gain
                curr_tank += gain

                if curr_tank < 0:
                    # Can't reach the next station from start to i
                    start_index = i + 1
                    curr_tank = 0

            return start_index if total_tank >= 0 else -1     