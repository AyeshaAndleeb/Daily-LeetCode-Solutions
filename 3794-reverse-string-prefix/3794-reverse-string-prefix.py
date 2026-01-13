class Solution:
    def reversePrefix(self, s: str, k: int) -> str:
        # Reverse first k characters + add remaining
        return s[:k][::-1] + s[k:]
