class Solution:
    def FactDigit(self, N):

        factorials = [1]
        for i in range(1, 10):
            factorials.append(factorials[-1] * i)

        def helper(number):
            if number == 0:
                return []

            for i in range(9, -1, -1):
                if factorials[i] <= number:
                    quo = number//factorials[i]
                    rem = number % factorials[i]
                    return helper(rem) + ([i] * quo)

        ans = helper(N)
        # ans.sort()
        ans = [str(x) for x in ans]

        for i in range(1, len(ans)):
            if ans[i] == '1':
                ans[i] = '0'
        
        return "".join(ans)

print(Solution().FactDigit(442721149))