class Solution:
    def romanToInt(self, s: str) -> int:
        roman  = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        total = 0
        prev_value = 0 #for tracking the previous value
        
        for char in reversed(s):
            current = roman[char]
            if current < prev_value:
                total -= current
            else: #otherwise we add
                total += current
                prev_value = current
        return total


        
        