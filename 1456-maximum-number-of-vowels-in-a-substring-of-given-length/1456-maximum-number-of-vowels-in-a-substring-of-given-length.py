class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels = {'a', 'e', 'i', 'o', 'u'}
        max_vowels = 0
        current_vowels = 0

        # Step 1: Count vowels in the first k-length window
        for i in range(k):
            if s[i] in vowels:
                current_vowels += 1
        max_vowels = current_vowels

        # Step 2: Slide the window across the string
        for i in range(k, len(s)):
            if s[i] in vowels:  # Add the new character
                current_vowels += 1
            if s[i - k] in vowels:  # Remove the old character
                current_vowels -= 1
            max_vowels = max(max_vowels, current_vowels)

        return max_vowels
