class Solution:
    def sortArrayByParityII(self, nums: List[int]) -> List[int]:
        n = len(nums)
        result = [0] * n
        
        even_index = 0
        odd_index = 1
        
        for num in nums:
            if num % 2 == 0:   # even number
                result[even_index] = num
                even_index += 2
            else:              # odd number
                result[odd_index] = num
                odd_index += 2
        
        return result
      