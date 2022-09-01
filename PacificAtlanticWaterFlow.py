from typing import List

class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        rows = len(heights)
        cols = len(heights[0])
        
        def dfs(i, j, prev, coords):
            if i < 0 or i >= rows or j < 0 or j >= cols:
                return
            
            if (i,j) in coords:
                return
            
            curr = heights[i][j]
            
            if curr < prev:
                return
            
            coords.add((i,j))
            
            dfs(i+1, j, curr, coords)
            dfs(i-1, j, curr, coords)
            dfs(i, j+1, curr, coords)
            dfs(i, j-1, curr, coords)
            
        pacific = set()
            
        for j in range(cols):
            dfs(0,j,0,pacific)
            
        for i in range(rows):
            dfs(i,0,0,pacific)
            
        atlantic = set()
        
        for j in range(cols):
            dfs(rows-1,j,0,atlantic)
        
        for i in range(rows):
            dfs(i,cols-1,0,atlantic)
            
        return list(pacific & atlantic)
            