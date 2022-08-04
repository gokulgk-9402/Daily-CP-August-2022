class Solution:
    def repeatedCharacter(self, s: str) -> str:
        seen = set()
        for ele in s:
            if ele in seen:
                return ele
            
            seen.add(ele)