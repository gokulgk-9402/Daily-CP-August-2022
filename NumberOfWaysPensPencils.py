class Solution:
    def waysToBuyPensPencils(self, total: int, cost1: int, cost2: int) -> int:
        ans = 0
        price1 = 0
        rem = total - price1
        
        while price1 <= total:
            ans += (rem // cost2 + 1)
            rem -= cost1
            price1 += cost1
            
        return ans