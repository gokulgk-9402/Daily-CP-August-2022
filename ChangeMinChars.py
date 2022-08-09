from typing import Counter


class Solution:
    def minCharacters(self, a: str, b: str) -> int:
        a_str = list(a)
        b_str = list(b)

        min_b = min(b_str)
        max_b = max(b_str)
        min_a = min(a_str)
        max_a = max(a_str)

        if min_b > max_a:
            return 0

        if min_a > max_b:
            return 0

        v1 = 0
        for letter in b_str:
            if letter <= max_a:
                v1 += 1

        v2 = 0
        for letter in a_str:
            if letter >= min_b:
                v2 += 1

        v1 = min(v1, v2)

        v2 = 0
        for letter in a_str:
            if letter <= max_b:
                v2 += 1
        
        v3 = 0
        for letter in b_str:
            if letter >= min_a:
                v3 += 1

        v2 = min(v2, v3)

        ctr = Counter(list(a+b))
        v3 = len(a+b) - max(ctr.values())

        return min(v1, v2, v3)

print(Solution().minCharacters(a = "aba", b = "caa"))