class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        set1 = set(nums1)  # Remove duplicates from nums1
        set2 = set(nums2)  # Remove duplicates from nums2
        return list(set1 & set2)  # Find common elements and convert to list