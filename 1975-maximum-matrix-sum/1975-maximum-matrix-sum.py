class Solution:
    def maxMatrixSum(self, matrix):
        total_abs_sum = 0          # sum of absolute values
        min_abs_value = float('inf')  # track smallest abs value
        negative_count = 0

        # traverse whole matrix
        for row in matrix:
            for value in row:
                # add absolute value to total
                total_abs_sum += abs(value)

                # update smallest absolute value
                min_abs_value = min(min_abs_value, abs(value))

                # count negatives
                if value < 0:
                    negative_count += 1

        # if negatives are even → all positives possible
        if negative_count % 2 == 0:
            return total_abs_sum

        # otherwise one smallest value must stay negative
        return total_abs_sum - 2 * min_abs_value
