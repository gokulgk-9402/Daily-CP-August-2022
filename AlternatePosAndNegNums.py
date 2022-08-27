#User function Template for python3

class Solution:
    def rearrange(self,arr, n):
        # code here
        pos = []
        neg = []
        
        size_pos = 0
        size_neg = 0
        
        for ele in arr:
            if ele < 0:
                neg.append(ele)
                size_neg += 1
            else:
                pos.append(ele)
                size_pos += 1
                
        i = 0
        j = 0
        
        sign = 1
        
        while i < size_pos and j < size_neg:
            if sign:
                arr[i+j] = pos[i]
                i += 1
                sign = 0
            else:
                arr[i+j] = neg[j]
                j += 1
                sign = 1
                
        while i < size_pos:
            arr[i+j] = pos[i]
            i += 1
            
        while j < size_neg:
            arr[i+j] = neg[j]
            j += 1