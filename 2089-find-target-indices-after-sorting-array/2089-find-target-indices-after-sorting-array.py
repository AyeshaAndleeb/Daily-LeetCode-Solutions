class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        nums.sort()          # step 1: sort
        result = []
        
        for i in range(len(nums)):   # step 2: check each index
            if nums[i] == target:
                result.append(i)
                
        return result
