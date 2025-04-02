class Solution:
    def maximumTripletValue(self, nums):
        n = len(nums)
        if n < 3:
            return 0  # Not enough elements for a triplet

        max_value = 0
        max_i = nums[0]  # Maximum value of nums[i] before j

        for j in range(1, n - 1):
            if max_i > nums[j]:  # Ensure (nums[i] - nums[j]) is positive
                max_k = max(nums[j+1:])  # Find max nums[k] after j
                max_value = max(max_value, (max_i - nums[j]) * max_k)

            max_i = max(max_i, nums[j])  # Update max_i for the next iteration

        return max_value
