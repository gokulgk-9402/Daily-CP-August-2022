from typing import List

class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        ans = []
        lp = len(potions)
        
        potions.sort()
        # print(potions)

        def bs(target):
            nonlocal lp
            left = 0
            right = lp -1
            
            while left <= right:
                mid = (left + right)//2
                if potions[mid] == target:
                    if potions[mid-1] == target:
                        right = mid -1
                    else:
                        return mid - 1
                
                elif potions[mid] < target:
                    left = mid +1
                else:
                    right = mid - 1
            # print(left, right)
            return right
            
        for spell in spells:
            if spell > success:
                ans.append(lp)
                continue
            req = success/spell
            pos = bs(req)
            # print(req, pos)
                    
            ans.append(lp - pos - 1)
            
        return ans

print(Solution().successfulPairs([40,11,24,28,40,22,26,38,28,10,31,16,10,37,13,21,9,22,21,18,34,2,40,40,6,16,9,14,14,15,37,15,32,4,27,20,24,12,26,39,32,39,20,19,22,33,2,22,9,18,12,5],[31,40,29,19,27,16,25,8,33,25,36,21,7,27,40,24,18,26,32,25,22,21,38,22,37,34,15,36,21,22,37,14,31,20,36,27,28,32,21,26,33,37,27,39,19,36,20,23,25,39,40], 600))