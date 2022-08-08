from typing import List

class Solution:
    def lexicalOrder(self, n: int) -> List[int]:
        ans = []
        
        def helper(i):
            if i > n:
                return

            ans.append(i)
            for j in range(10):
                helper(10*i + j)

        for i in range(1, 10):
            helper(i)

        return ans

print(Solution().lexicalOrder(13))