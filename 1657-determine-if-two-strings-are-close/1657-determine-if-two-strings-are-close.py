from collections import Counter
class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:

        # Step 1: Check if lengths are different
        if len(word1) != len(word2):
            return False
        
        # Step 2: Count frequency of characters
        freq1 = Counter(word1)
        freq2 = Counter(word2)
        
        # Step 3: Unique character set check
        if set(freq1.keys()) != set(freq2.keys()):
            return False
        
        # Step 4: Compare sorted frequency values
        if sorted(freq1.values()) != sorted(freq2.values()):
            return False
        
        return True