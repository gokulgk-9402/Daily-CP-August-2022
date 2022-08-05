class Solution:
    def xShape(self, grid):
        rows = len(grid)
        cols = len(grid[0])

        def dfs(r, c):
            nonlocal rows, cols
            grid[r][c] = 'O'
            if r != 0 and grid[r-1][c] == 'X':
                dfs(r-1, c)
            if r != rows-1 and grid[r+1][c] == 'X':
                dfs(r+1, c)
            if c != 0 and grid[r][c-1] == 'X':
                dfs(r, c-1)
            if c != cols - 1 and grid[r][c+1] == 'X':
                dfs(r, c+1)

            return


        ans = 0

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 'X':
                    ans += 1
                    dfs(i,j)

        return ans

print(Solution().xShape([['X','O','X'],['O','X','O'],['X','X','X']]))

