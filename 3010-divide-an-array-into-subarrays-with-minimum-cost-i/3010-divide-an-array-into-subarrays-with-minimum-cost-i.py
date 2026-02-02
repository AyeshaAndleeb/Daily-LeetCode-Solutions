class Solution:
    def minimumCost(self, nums):
        total_cost = nums[0]

        first_min = float('inf')
        second_min = float('inf')

        for num in nums[1:]:
            if num < first_min:
                second_min = first_min   
                first_min = num
            elif num < second_min:
                second_min = num

        total_cost += first_min + second_min

        return total_cost