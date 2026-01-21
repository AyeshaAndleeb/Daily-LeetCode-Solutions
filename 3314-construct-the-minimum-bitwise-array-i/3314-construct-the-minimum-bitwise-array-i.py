from typing import List

class Solution:
    def minBitwiseArray(self, nums: List[int]) -> List[int]:
        ans = []

        for target in nums:
            found = -1
            for x in range(target):
                if (x | (x + 1)) == target:
                    found = x
                    break
            ans.append(found)

        return ans
