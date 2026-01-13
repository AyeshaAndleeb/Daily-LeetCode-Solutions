class Solution:
    def numJewelsInStones(self, J: str, S: str) -> int:
        return sum(S.count(jewel) for jewel in J)
