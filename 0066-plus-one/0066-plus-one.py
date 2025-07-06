class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        number_str = ""
        for d in digits:
            number_str += str(d)

        number = int(number_str)
        number += 1

        result = []
        for ch in str(number):
            result.append(int(ch))

        return result
        