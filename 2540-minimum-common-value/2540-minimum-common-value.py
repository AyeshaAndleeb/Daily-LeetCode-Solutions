class Solution:
    def getCommon(self, nums1: List[int], nums2: List[int]) -> int:
        common = set(nums1) & set(nums2)
        return min(common) if common else -1
            

        