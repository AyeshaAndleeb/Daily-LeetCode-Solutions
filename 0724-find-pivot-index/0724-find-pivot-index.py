class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        total_sum = sum(nums)  # Get the total sum of the array
        left_sum = 0  # Track left sum

        for i in range(len(nums)):
            if left_sum == total_sum - left_sum - nums[i]:  # Check pivot condition
                return i
            left_sum += nums[i]  # Update left sum
        
        return -1  # No pivot index found
