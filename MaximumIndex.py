#User function Template for python3

class Solution:
    #Complete this function
    # Function to find the maximum index difference.
    def maxIndexDiff(self,A, N): 
        left_min = [A[0]]
        
        for i in range(1, N):
            left_min.append(min(left_min[-1], A[i]))

        print(left_min)
        j = N - 1
        i = N - 1

        max_diff = 0

        while i > -1 and j > -1:
            if A[i] >= left_min[j]:
                max_diff = max(max_diff, i - j)
                j -= 1
            else:
                i -= 1

        return max_diff



print(Solution().maxIndexDiff([34,8,10,3,2,80,30,33,1], 9))