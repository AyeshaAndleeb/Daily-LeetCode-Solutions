from typing import List

class Solution:
    def sumFourDivisors(self, nums: List[int]) -> int:
        total_sum = 0 
        
        for n in nums:
            div_sum = 0 
            count = 0
            
            for i in range(1, int(n**0.5) + 1):
                
                if n % i == 0:
                    j = n // i

                    count += 1
                    div_sum += i

                    if j != i:
                        count += 1
                        div_sum += j
                
                # agar 4 se zyada ho jayein -> chor do
                if count > 4:
                    break
            
            # loop ke BAAD check karna hai
            if count == 4:
                total_sum += div_sum

        return total_sum
