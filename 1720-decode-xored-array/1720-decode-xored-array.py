class Solution:
    def decode(self, encoded: List[int], first: int) -> List[int]:
        

        original = [first]  # Step 1: Initialize with first element
        for num in encoded:
            original.append(original[-1] ^ num)  # Step 2: XOR operation
        return original
    