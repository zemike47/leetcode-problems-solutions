class Solution:
    def combinationSum(self, candidates: list[int], target: int) -> list[list[int]]:
        result = []

        def backtrack(start, path, total):
            if total == target:
                result.append(path[:])  # Found a valid combination
                return
            if total > target:
                return  # Exceeded the sum, stop this path

            for i in range(start, len(candidates)):
                path.append(candidates[i])
                backtrack(i, path, total + candidates[i])  # Not i + 1 because we can reuse same element
                path.pop()  # Backtrack

        backtrack(0, [], 0)
        return result