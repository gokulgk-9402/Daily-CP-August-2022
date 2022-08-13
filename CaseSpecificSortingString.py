class Solution:

    #Function to perform case-specific sorting of strings.
    def caseSort(self,s,n):
        #code here
        cases = []
        lowers = []
        uppers = []
        
        for char in s:
            if ord('A') <= ord(char) <= ord('Z'):
                cases.append(1)
                uppers.append(char)
            else:
                cases.append(0)
                lowers.append(char)
                
        lowers.sort()
        uppers.sort()
        
        i = j = 0
        ans = ""
        
        while i + j < n:
            if cases[i+j] == 1:
                ans += uppers[i]
                i += 1
            else:
                ans += lowers[j]
                j += 1
                
        return ans