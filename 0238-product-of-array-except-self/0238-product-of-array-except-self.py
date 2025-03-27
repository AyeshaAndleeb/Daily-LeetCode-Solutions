class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        answer = [1] * n  # Step 1: Initialize output array with 1s

        # Step 2: Compute prefix products
        prefix = 1
        for i in range(n):
            answer[i] = prefix  # Store the prefix product
            prefix *= nums[i]   # Update prefix

        # Step 3: Compute suffix products and multiply
        suffix = 1
        for i in range(n - 1, -1, -1):
            answer[i] *= suffix  # Multiply by suffix product
            suffix *= nums[i]    # Update suffix

        return answer
