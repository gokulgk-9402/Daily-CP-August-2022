#User function Template for python3 

class Solution:
    def DistinctSum(self, nums):
		# Code here
        total = sum(nums)
        length = len(nums)

        dp = [[False for _ in range(total + 1)] for _ in range(length + 1)]

        for i in range(length + 1):
            dp[i][0] = True

        for i in range(1, length + 1):
            dp[i][nums[i - 1]] = True

            for j in range(1, total + 1):
                if dp[i - 1][j]:
                    dp[i][j] = True
                    dp[i][j + nums[i - 1]] = True

        return [j for j in range(total + 1) if dp[length][j]]


print(Solution().DistinctSum([1,2]))