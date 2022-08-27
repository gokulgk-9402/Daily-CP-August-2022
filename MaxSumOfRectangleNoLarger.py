from bisect import bisect_left, insort
from typing import List

class Solution:
    def maxSumSubmatrix(self, matrix: List[List[int]], k: int) -> int:
        rows = len(matrix)
        cols = len(matrix[0])

        ans = -1 * float("inf")

        for left in range(cols):
            row_sums = [0 for _ in range(rows)]

            for right in range(left, cols):
                col_sums = [0]
                col_sum = 0

                for i in range(rows):
                    row_sums[i] += matrix[i][right]
                    col_sum += row_sums[i]
                    diff = col_sum - k
                    index = bisect_left(col_sums, diff)
                    if index < len(col_sums):
                        if col_sums[index] == diff:
                            return k
                        else:
                            ans = max(ans, col_sum - col_sums[index])

                    insort(col_sums, col_sum)

        return ans
