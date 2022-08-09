class Solution:
    def makeGood(self, s: str) -> str:
        length = len(s)

        def helper(str, l):
            # print(str)
            if l == 0 or l == 1:
                return str

            i = 0
            while i < l-1:
                if ord(str[i]) - ord(str[i+1]) == 32 or ord(str[i+1]) - ord(str[i]) == 32:
                    return helper(str[:i] + str[i+2:], l-2)
                i += 1

            return str

        return helper(s, length)


print(Solution().makeGood(s = "leEeetcode"))
            