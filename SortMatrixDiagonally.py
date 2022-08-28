from typing import List

class Solution:
    def diagonalSort(self, mat: List[List[int]]) -> List[List[int]]:
        
        rows = len(mat)
        cols = len(mat[0])
        
        for start in range(cols):
            temp = []
            i = 0
            while i < rows and start + i < cols:
                temp.append(mat[i][start + i])
                i += 1
            # print(temp)
            temp.sort()
            i = 0
            while i < rows and start + i < cols:
                mat[i][start + i] = temp[i]
                i += 1
                
        # print(mat)
                
        for start in range(rows):
            temp = []
            i = 0
            while start + i < rows and i < cols:
                temp.append(mat[start+i][i])
                i += 1
            # print(temp)
            temp.sort()
            i = 0

            while i < cols and start + i < rows:
                mat[start + i][i] = temp[i]
                i += 1

        return mat

        # print(mat)

matrix = [[11,25,66,1,69,7],[23,55,17,45,15,52],[75,31,36,44,58,8],[22,27,33,25,68,4],[84,28,14,11,5,50]]
print(Solution().diagonalSort(matrix))
# print(matrix)