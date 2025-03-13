from typing import List

class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        n = len(grid)  # Get the size of the grid (n x n)
        total_numbers = n * n
        count = {}
        a, b = -1, -1  # Initialize missing and repeated values

        # Step 1: Flatten the grid into a list
        flatten_list = []
        for row in grid:
            for num in row:
                flatten_list.append(num)

        # Step 2: Count occurrences of each number
        for num in flatten_list:
            count[num] = count.get(num, 0) + 1  # Increment count of each number

        # Step 3: Find the repeating and missing numbers
        for i in range(1, total_numbers + 1):  # Check from 1 to n²
            if i in count:
                if count[i] == 2:
                    a = i  # Found repeated number
            else:
                b = i  # Found missing number

        return [a, b]
