class Solution:
    def isSumEqual(self, firstWord, secondWord, targetWord):
        
        def wordToNumber(word):
            num = ""
            for char in word:
                num += str(ord(char) - ord('a'))  # a->0, b->1, ...
            return int(num)
        
        num1 = wordToNumber(firstWord)
        num2 = wordToNumber(secondWord)
        numTarget = wordToNumber(targetWord)
        
        return num1 + num2 == numTarget
