from typing import List

class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        result = [""] * len(s)  # Step 1: Create empty list
        for i in range(len(s)):  # Step 2: Assign characters to correct positions
            result[indices[i]] = s[i]
        return "".join(result)  # Step 3: Convert list to string

        