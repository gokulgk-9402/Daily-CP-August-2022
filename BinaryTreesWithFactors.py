class Solution:
    def numFactoredBinaryTrees(self, arr: List[int]) -> int:
        n = len(arr)
        arr.sort()
        mem = [1] * n
        index = {x:i for i, x in enumerate(arr)}
        
        for i, x in enumerate(arr):
            for j in range(i):
                if x % arr[j] == 0:
                    right = x / arr[j]
                    if right in index:
                        mem[i] += mem[j] * mem[index[right]]
        
        return sum(mem) % (10**9 + 7)