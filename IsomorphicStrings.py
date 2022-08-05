class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        keys = {}
        seen = set()
        for i in range(len(s)):
            if s[i] in keys:
                if keys[s[i]] != t[i]:
                    return False
            else:
                if t[i] in seen:
                    return False
                keys[s[i]] = t[i]
                seen.add(t[i])

        return True

print(Solution().isIsomorphic(s = "badc", t = "baba"))