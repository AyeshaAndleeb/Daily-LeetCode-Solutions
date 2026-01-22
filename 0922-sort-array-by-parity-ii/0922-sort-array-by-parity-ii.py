class Solution:
    def sortArrayByParityII(self, nums):
        i = 0  # even index pointer
        j = 1  # odd index pointer
        n = len(nums)

        while i < n and j < n:
            if nums[i] % 2 == 0:
                i += 2
            elif nums[j] % 2 == 1:
                j += 2
            else:
                nums[i], nums[j] = nums[j], nums[i]
                i += 2
                j += 2

        return nums
