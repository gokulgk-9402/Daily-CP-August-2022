from collections import defaultdict
from typing import List

class Solution:
    def minSubarray(self, nums: List[int], p: int) -> int:
        initial = sum(nums)
        to_rmv = initial % p
        
        if not to_rmv:
            return 0

        curr = 0
        mem = {}
        mem[0] = -1
        l = len(nums)
        ans = l

        for i in range(l):
            curr += nums[i]
            curr_mod = curr%p

            temp = (curr - to_rmv) % p

            if temp in mem:
                if i - mem[temp] < ans:
                    ans = i - mem[temp]

            mem[curr_mod] = i

        if ans < l:
            return ans
        
        return -1

print(Solution().minSubarray(nums = [3,1,4,2], p = 6))