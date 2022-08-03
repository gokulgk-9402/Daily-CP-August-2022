from typing import List

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        if len(nums) == 1:
            return [[],[nums[0]]]
        
        sol = []
        
        sol1 = self.subsets(nums[1:])
        # print(sol1)
        for s in sol1:
            sol.append(s)
            sol.append([nums[0]] + s)
            
        return sol