class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:

        sorted_nums = sorted(nums)  # Sort the array
        num_index = {}  # Dictionary to store the smallest index
        for i, num in enumerate(sorted_nums):
            if num not in num_index:  # Store first occurrence only
                num_index[num] = i
        
        return [num_index[num] for num in nums]

