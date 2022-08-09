from typing import Counter

class Solution:
    def minCharacters(self, a: str, b: str) -> int:
        counterA = Counter(a)
        counterB = Counter(b)

        l1 = [counterA.get("a",0)]
        l2 = [counterB.get("a", 0)]

        lena = len(a)
        lenb = len(b)

        v3 = lena + lenb - max(counterA.values()) - max(counterB.values())

        v1 = v2 = lena + lenb

        for i in range(1, 26):
            l1.append(counterA.get(chr(97+i), 0) + l1[-1])
            l2.append(counterB.get(chr(97+i), 0) + l2[-1])

            v1 = min(lena - l1[i-1] + l2[i-1], v1)
            v2 = min(lenb - l2[i-1] + l1[i-1], v2)

        return min(v1, v2, v3)

print(Solution().minCharacters(a = "ace", b = "abe"))