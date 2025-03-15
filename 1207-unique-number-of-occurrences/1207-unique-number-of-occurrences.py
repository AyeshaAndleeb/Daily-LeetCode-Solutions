class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        freq = Counter(arr)  # Count occurrences of each number
        return len(set(freq.values())) == len(freq)
        