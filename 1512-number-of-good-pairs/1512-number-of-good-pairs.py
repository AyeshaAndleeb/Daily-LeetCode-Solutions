from collections import defaultdict
class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        freq = defaultdict(int)
        count = 0
        for num in nums:
            count += freq[num]   # add how many times we've seen this number before
            freq[num] += 1       # update frequency
        return count
