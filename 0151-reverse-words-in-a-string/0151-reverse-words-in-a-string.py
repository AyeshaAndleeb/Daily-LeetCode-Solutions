class Solution:
    def reverseWords(self, s: str) -> str :
        return " ".join(s.split()[::-1])  # Splits, reverses, and joins words
        