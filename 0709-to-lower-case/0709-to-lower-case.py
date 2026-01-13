class Solution:
    def toLowerCase(self, s: str) -> str:
        result = []
        for char in s:
            # check if uppercase
            if 'A' <= char <= 'Z':
                # convert to lowercase
                result.append(chr(ord(char) + 32))
            else:
                result.append(char)
        return ''.join(result)
