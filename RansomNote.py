class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        temp = Counter(magazine)
        for i in ransomNote:
            if i in temp:
                if temp[i] != 0:
                    temp[i] -= 1
                    continue
            return False
        return True