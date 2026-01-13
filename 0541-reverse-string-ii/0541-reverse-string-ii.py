class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        s = list(s)   # string ko list banaya (kyun ke string immutable hoti hai)
        
        for i in range(0, len(s), 2*k):
            s[i:i+k] = reversed(s[i:i+k])
        
        return "".join(s)
