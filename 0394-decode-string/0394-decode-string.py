class Solution:
    def decodeString(self, s: str) -> str:
        str_stack = []
        num_stack = []
        curr_str = ""
        num = 0

        for char in s:
            if char.isdigit():
                num = num * 10 + int(char)  # handle multi-digit numbers
            elif char == '[':
                num_stack.append(num)
                str_stack.append(curr_str)
                num = 0
                curr_str = ""
            elif char == ']':
                repeat = num_stack.pop()
                prev_str = str_stack.pop()
                curr_str = prev_str + repeat * curr_str
            else:
                curr_str += char

        return curr_str
