class Solution:
    def minimumCost(self, nums):
        total_cost = nums[0]        # pehla element hamesha add
        rest = nums[1:]             # baki array
        rest.sort()                 # chote se bada sort kar do
        total_cost += rest[0]       # second subarray ka smallest
        total_cost += rest[1]       # third subarray ka next smallest
        return total_cost

