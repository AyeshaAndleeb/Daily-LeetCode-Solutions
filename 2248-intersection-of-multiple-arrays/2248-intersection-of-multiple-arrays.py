class Solution:
    def intersection(self, nums: List[List[int]]) -> List[int]:

        # Convert each list to a set
        sets = [set(arr) for arr in nums]
        
        # Find the intersection of all sets
        common_elements = set.intersection(*sets)
        
        # Return the sorted result
        return sorted(common_elements)


        