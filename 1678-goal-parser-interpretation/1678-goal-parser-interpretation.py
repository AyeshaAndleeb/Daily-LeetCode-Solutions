class Solution:
    def interpret(self, command: str) -> str:
        i = 0
        res = ""
        while i < len(command):
            if command[i] == 'G':
                res += "G"
                i += 1
            elif command[i:i+2] == "()":
                res += "o"
                i += 2
            else:  # must be "(al)"
                res += "al"
                i += 4
        return res
