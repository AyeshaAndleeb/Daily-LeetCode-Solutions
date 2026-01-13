class Solution:
    def arrayRankTransform(self, arr):
        
        # step 1: array ka copy bnao aur usko sort karo
        sorted_arr = sorted(arr)
        
        # step 2: empty dictionary (number → rank)
        rank = {}
        
        # step 3: rank dena start karo
        current_rank = 1
        
        for num in sorted_arr:
            # agar number pehle se rank nahi hua
            if num not in rank:
                rank[num] = current_rank
                current_rank += 1
        
        # step 4: original array ko ranks se replace karo
        result = []
        for num in arr:
            result.append(rank[num])
        
        return result
