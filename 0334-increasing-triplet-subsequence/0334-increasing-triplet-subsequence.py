class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        first = float('inf')  # Smallest number (initialized to infinity)
        second = float('inf') # Second smallest number (initialized to infinity)

        for num in nums:
            if num <= first:
                first = num  # Update smallest number
            elif num <= second:
                second = num  # Update second smallest number
            else:
                return True  # Found increasing triplet (first < second < num)
        
        return False  # No triplet found
      