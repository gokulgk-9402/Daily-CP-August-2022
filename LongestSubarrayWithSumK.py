#User function Template for python3

class Solution:
    def lenOfLongSubarr (self, arr, n, k) : 
        #Complete the function
        ans = 0
        curr = 0

        mem = {0: -1}
        
        for i in range(n):
            curr += arr[i]
            if (curr-k) in mem:
                ans = max(ans, i - mem[curr-k])

            if curr not in mem:
                mem[curr] = i

        # print(mem)

        return ans

print(Solution().lenOfLongSubarr([10, 5, 2, 7, 1, 9], 6, 15))
