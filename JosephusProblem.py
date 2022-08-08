
class Solution:
    def josephus(self,n,k):
        #Your code here
        
        def helper(n):
            if n == 1:
                return 1
            
            return (helper(n-1) + k -1)% n + 1
            
        return helper(n)