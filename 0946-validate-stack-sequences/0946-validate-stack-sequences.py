class Solution:
    def validateStackSequences(self, pushed, popped):
        
        stack = []
        j = 0   # pointer for popped
        
        for x in pushed:
            stack.append(x)   # push
            
           
            while stack and stack[-1] == popped[j]:
                stack.pop()
                j += 1
        
        return not stack
