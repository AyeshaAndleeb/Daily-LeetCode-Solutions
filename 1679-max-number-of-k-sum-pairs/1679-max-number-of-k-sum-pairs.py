from collections import Counter

class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        freq = Counter(nums)  # Count the occurrences of each number
        operations = 0
        
        for num in list(freq.keys()):
            complement = k - num  # Find the pair number
            
            if complement in freq:
                if complement == num:
                    pairs = freq[num] // 2  # If both numbers are the same, take half
                else:
                    pairs = min(freq[num], freq[complement])  # Take min count of the two
                
                operations += pairs
                freq[num] -= pairs
                freq[complement] -= pairs

        return operations
