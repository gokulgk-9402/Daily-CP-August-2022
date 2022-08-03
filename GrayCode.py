class Solution:
    def grayCode(self, n: int) -> List[int]:
        if n == 1:
            return [0, 1]
        
        ans = self.grayCode(n-1)
        # print(ans)
        a2 = ans[:]
        # print(a2)
        a2.reverse()
        for i in range(len(a2)):
            a2[i] += 2 ** (n - 1)
            
        ans += a2
        
        return ans