class Solution:
    def minimumPairRemoval(self, nums: List[int]) -> int:
        ops = 0
        
        def is_sorted(arr):
            for i in range(1, len(arr)):
                if arr[i] < arr[i-1]:
                    return False
            return True
        
        while not is_sorted(nums):
            # Step 1: Find leftmost pair with minimum sum
            min_sum = float('inf')
            min_index = 0
            for i in range(len(nums)-1):
                pair_sum = nums[i] + nums[i+1]
                if pair_sum < min_sum:
                    min_sum = pair_sum
                    min_index = i
            
            # Step 2: Replace pair with sum
            nums[min_index] = nums[min_index] + nums[min_index+1]
            nums.pop(min_index+1)  # remove second element
            ops += 1
            
        return ops
