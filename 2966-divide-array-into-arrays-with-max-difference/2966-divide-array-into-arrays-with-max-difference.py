class Solution:
    def divideArray(self, nums, k):
        nums.sort()
        result = []

        for i in range(0, len(nums), 3):
            if nums[i+2] - nums[i] > k:
                return []
            result.append([nums[i], nums[i+1], nums[i+2]])

        return result
