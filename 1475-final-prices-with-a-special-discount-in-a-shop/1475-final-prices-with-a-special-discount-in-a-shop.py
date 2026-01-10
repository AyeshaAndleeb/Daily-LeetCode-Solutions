class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        n = len(prices)
        answer = prices[:]   # copy of prices

        for i in range(n):
            for j in range(i + 1, n):
                if prices[j] <= prices[i]:
                    answer[i] = prices[i] - prices[j]
                    break   # pehla discount mil gaya

        return answer
