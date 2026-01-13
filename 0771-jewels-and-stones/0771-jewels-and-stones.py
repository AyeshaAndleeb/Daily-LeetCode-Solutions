class Solution:
    def numJewelsInStones(self, J: str, S: str) -> int:
        jewel_set = set(J)  # fast lookup
        count = 0
        
        for stone in S:
            if stone in jewel_set:
                count += 1
        
        return count
