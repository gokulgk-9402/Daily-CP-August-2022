class Solution:
    def minStepToReachTarget(self, KnightPos, TargetPos, N):
		#Code here
        visited = [[0 for _ in range(N+1)] for _ in range(N+1)]
        queue = []

        x_vals = [2, 2, -2, -2, -1, -1, 1, 1]
        y_vals = [1, -1, 1, -1, 2, -2, 2, -2]

        queue.append([KnightPos[0], KnightPos[1], 0])
        
        visited[KnightPos[0]][KnightPos[1]] = 1

        while len(queue) != 0:
            curr = queue.pop(0)

            if curr[0] == TargetPos[0] and curr[1] == TargetPos[1]:
                return curr[2]

            nxt = [0, 0]

            for i in range(8):
                nxt[0] = curr[0] + x_vals[i]
                nxt[1] = curr[1] + y_vals[i]

                if nxt[0] < 1 or nxt[0] > N or nxt[1] < 1 or nxt[1] > N:
                    continue

                if visited[nxt[0]][nxt[1]] == 1:
                    continue

                queue.append([nxt[0], nxt[1], curr[2] + 1])
                visited[nxt[0]][nxt[1]] = 1

        return -1