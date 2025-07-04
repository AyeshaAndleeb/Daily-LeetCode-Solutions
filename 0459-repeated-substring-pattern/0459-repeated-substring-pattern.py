class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        n = len(s)  # string ki length

        for i in range(1, n // 2 + 1):   # Half tak check karo
            if n % i == 0:               # Agar string i se divide hoti hai
                sub = s[:i]              # Prefix substring lo
                if sub * (n // i) == s:  # Kya sub ko repeat karne se s milta?
                    return True

        return False