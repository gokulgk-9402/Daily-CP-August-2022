#User function Template for python3

class Solution:
    def countFriendsPairings(self, n):
        # code here 

        mem = [0, 1, 2, 4]
        length = 4

        def dp(num):
            nonlocal length
            if num < length:
                return mem[num]

            mem.append((dp(num-1) + (num - 1) * dp(num - 2)) % (10**9 + 7))
            length += 1

            return mem[num]

        return dp(n)

print(Solution().countFriendsPairings(4))