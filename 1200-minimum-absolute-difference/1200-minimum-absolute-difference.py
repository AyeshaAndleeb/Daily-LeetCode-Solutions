class Solution:
    def minimumAbsDifference(self, arr):
        arr.sort()                  # Step 1
        min_diff = float('inf')
        result = []

        # Step 2: minimum difference find karo
        for i in range(len(arr) - 1):
            diff = arr[i+1] - arr[i]
            min_diff = min(min_diff, diff)

        # Step 3: pairs collect karo
        for i in range(len(arr) - 1):
            if arr[i+1] - arr[i] == min_diff:
                result.append([arr[i], arr[i+1]])

        return result
