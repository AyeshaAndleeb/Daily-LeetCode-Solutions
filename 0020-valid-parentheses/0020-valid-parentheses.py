class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        mapping = {')': '(', '}': '{', ']': '['}
        
        for char in s:
            if char in mapping:
                if not stack or stack.pop() != mapping[char]:
                    return False
            else:
                stack.append(char)
        
        return not stack  # return not stack ensures that all opening brackets have matching closing brackets by checking if the stack is empty at the end.

#stack = []  
#print(not stack)  # True, because the list is empty

#stack.append('(')  
#print(not stack)  # False, because the list is not empty