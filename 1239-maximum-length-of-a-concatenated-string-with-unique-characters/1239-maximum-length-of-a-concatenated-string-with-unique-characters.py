class Solution:
    def maxLength(self, arr):
        def backtrack(index, path):
            max_len = len(path)

            for i in range(index, len(arr)):
                if len(set(arr[i])) != len(arr[i]):
                    continue

                if set(arr[i]) & set(path):
                    continue

                max_len = max(max_len,
                              backtrack(i+1, path + arr[i]))

            return max_len

        return backtrack(0, "")