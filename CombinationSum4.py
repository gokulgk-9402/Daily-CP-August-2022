from typing import List

class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        mem = [0 for _ in range(target+1)]
        
        mem[0] = 1
        
        for i in range(1, target+1):
            for num in nums:
                if i - num < 0:
                    continue
                    
                mem[i] += mem[i-num]
                
        return mem[target]