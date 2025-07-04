class Solution:
    def average(self, salary: List[int]) -> float:
        total = sum(salary)              # sab salaries ka total
        minimum = min(salary)            # min salary
        maximum = max(salary)            # max salary
        count = len(salary) - 2          # exclude min & max

        return (total - minimum - maximum) / count
        