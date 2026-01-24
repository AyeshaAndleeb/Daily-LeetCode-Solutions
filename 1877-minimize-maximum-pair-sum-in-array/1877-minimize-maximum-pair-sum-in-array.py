class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        nums.sort()
        n = len(nums)
        i = 0
        j = n - 1
        maxSum = 0
        while i <= j:
            pairSum = nums[i] + nums[j]
            maxSum = max(pairSum, maxSum)
            i+=1
            j-=1
        return maxSum
        