class Solution:
    def minimumSteps(self, s: str) -> int:
        swaps = 0
        black = 0   # count of black balls seen so far

        for ch in s:
            if ch == '0':          # white ball
                swaps += black    # move this white to left
            else:                  # black ball
                black += 1

        return swaps
