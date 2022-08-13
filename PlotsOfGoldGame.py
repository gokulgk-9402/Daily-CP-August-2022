class Solution:
    def maxCoins(self,arr, n):
        # Code here

        mem = [[None for _ in range(n)] for _ in range(n)]

        for i in range(n):
            mem[i][i] = arr[i]
        
        def helper(i, j):
            if mem[i][j] is not None:
                return mem[i][j]

            if i == j - 1:
                mem[i][j] = max(arr[i], arr[j])
                return mem[i][j]

            mem[i][j] = max(arr[i] + min(helper(i+2, j), helper(i+1, j-1)), arr[j] + min(helper(i+1, j-1), helper(i, j-2)))
            return mem[i][j]

        return helper(0, n-1)


print(Solution().maxCoins([8, 15, 3, 7], 4))