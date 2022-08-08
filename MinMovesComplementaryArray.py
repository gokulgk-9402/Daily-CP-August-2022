from typing import List
from collections import defaultdict


class Solution:
    def minMoves(self, nums: List[int], limit: int) -> int:
        sums = defaultdict(int)
        n = len(nums)
        intervals = [0] * (2*limit + 2)
        for i in range(n//2):
            sums[nums[i] + nums[n-i-1]] += 1
            intervals[min(nums[i], nums[n-1-i]) + 1] += 1
            intervals[max(nums[i], nums[n-1-i]) + limit + 1] -= 1

        ans = float("inf")
        for i in range(1, len(intervals)):
            intervals[i] += intervals[i-1]
            ans = min(ans, 2*(n//2 - intervals[i]) + intervals[i] - sums[i])

        return ans
    

print(Solution().minMoves(nums = [1,2,4,3], limit = 4))
