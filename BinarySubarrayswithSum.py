from collections import defaultdict
from typing import Counter, List

class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        
        prefixes = [0]
        
        for num in nums:
            prefixes.append(prefixes[-1] + num)

        count = defaultdict(int)

        ans = 0
        for prefix in prefixes:
            ans += count[prefix]
            count[prefix + goal] += 1

        return ans

print(Solution().numSubarraysWithSum(nums = [0, 0, 0, 1,0,0,0,0], goal = 2))