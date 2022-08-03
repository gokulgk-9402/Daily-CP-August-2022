from typing import Counter, List

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for row in board:
            counter = Counter(row)
            # print(counter)
            for key in counter:
                if key == ".":
                    continue
                if counter[key] > 1:
                    return False

        for i in range(9):
            col = [board[x][i] for x in range(9)]
            counter = Counter(col)
            for key in counter:
                if key == ".":
                    continue
                if counter[key] > 1:
                    return False

        for i in range(3):
            for j in range(3):
                square = [board[3*i][x] for x in range(3*j, 3*j + 3)]
                square += [board[3*i + 1][x] for x in range(3*j, 3*j + 3)]
                square += [board[3*i + 2][x] for x in range(3*j, 3*j + 3)]
                
                counter = Counter(square)
                for key in counter:
                    if key == ".":
                        continue
                    if counter[key] > 1:
                        return False

        return True


print(Solution().isValidSudoku([["8","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]))