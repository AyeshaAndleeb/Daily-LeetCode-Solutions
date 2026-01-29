class Solution:
    def combine(self, n: int, k: int):
        result = []

        def backtrack(start, current):
            # BASE CASE
            if len(current) == k:
                result.append(current.copy())
                return

            for i in range(start, n + 1):
                # choose
                current.append(i)

                # explore
                backtrack(i + 1, current)

                # un-choose (backtracking)
                current.pop()

        backtrack(1, [])
        return result
