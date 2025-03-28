class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        output = [1] * n  # Initialize output array
        
        for i in range(n):
            product = 1
            for j in range(n):
                if i != j:  # Exclude the current element
                    product *= nums[j]
            output[i] = product
        
        return output


