class Solution:
    
    #Function to find minimum number of attempts needed in 
    #order to find the critical floor.
    def eggDrop(self,n, k):
        # code here
        
        mem = [[-1 for _ in range(k+1)] for _ in range(n+1)]
        
        for i in range(1, k+1):
            mem[1][i] = i
        
        for i in range(1, n+1):
            mem[i][0] = 0
            mem[i][1] = 1

        def dp(n, k):
            print(n, k)
            if mem[n][k] != -1:
                return mem[n][k]

            for i in range(2, n+1):
                for j in range(2, k+1):
                    minimum = k+1
                    for x in range(1, j+1):
                        res = 1+  max(mem[i-1][x-1], mem[i][j-x])
                        if minimum > res:
                            minimum = res

                        mem[i][j] = minimum

            return mem[n, k]

        return dp(n,k)