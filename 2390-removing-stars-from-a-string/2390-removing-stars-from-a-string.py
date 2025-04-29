class Solution:
    def removeStars(self, s: str) -> str:
        stack = []
        
        for ch in s:
            if ch == '*':
                stack.pop()  # Remove last character
            else:
                stack.append(ch)  # Add character
        
        return ''.join(stack)  # Convert list back to string
