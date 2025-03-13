class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}  # Dictionary to store numbers and their indices
        
        for i, num in enumerate(nums):  # Loop through each number with its index
            complement = target - num  # The number needed to reach the target
            if complement in hashmap:  # Check if the complement exists in hashmap
                return [hashmap[complement], i]  # Return indices of the pair
            hashmap[num] = i  # Store the number with its index
