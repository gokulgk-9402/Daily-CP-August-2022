#User function Template for python3
class Solution:

    def immediateSmaller(self,arr,n):
		# code here
        for i in range(n - 1):
            arr[i] = arr[i+1] if arr[i+1] < arr[i] else -1
		    
        arr[n-1] = -1
		
n = int(input())
arr = [int(x) for x in input().split()]
Solution().immediateSmaller(arr, n)
print(arr)