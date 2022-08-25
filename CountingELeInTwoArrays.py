import bisect as bt

#User function Template for python3

class Solution:
    def countEleLessThanOrEqual(self,arr1,n1,arr2,n2):
        #returns the required output
        arr2.sort()
        ans = []

        for ele in arr1:
            ans.append(bt.bisect(arr2, ele))

        return ans