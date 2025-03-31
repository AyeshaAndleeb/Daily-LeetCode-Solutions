class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        # Compute sum of the first k elements (initial window)
        window_sum = sum(nums[:k])
        max_sum = window_sum

        # Slide the window across the array
        for i in range(k, len(nums)):
            window_sum += nums[i] - nums[i - k]  # Add new element, remove old element
            max_sum = max(max_sum, window_sum)

        # Return maximum average
        return max_sum / k
