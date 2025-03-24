from typing import List

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        left = 0  # Pointer to track position of next non-zero element
        for right in range(len(nums)):  # Iterate through the array
            if nums[right] != 0:  # If non-zero, swap with nums[left]
                nums[left], nums[right] = nums[right], nums[left]
                left += 1  # Move left pointer forward
