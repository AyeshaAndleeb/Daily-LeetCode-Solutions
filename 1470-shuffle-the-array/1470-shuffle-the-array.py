class Solution:
    def shuffle(self, nums, n):
        first = nums[:n]
        second = nums[n:]
        shuffled = []

        for i in range(n):
            shuffled.append(first[i])
            shuffled.append(second[i])
        
        return shuffled
