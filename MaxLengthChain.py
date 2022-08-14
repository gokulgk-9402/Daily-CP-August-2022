#User function Template for python3

'''
class Pair(object):
    def __init__(self, a, b):
        self.a = a
        self.b = b
'''
# class Solution:
#     def maxChainLen(self,Parr, n):
#         # Parr:  list of pair
#         #code here
#         mem = {}

#         def helper(prev, pos):
#             if (prev, pos) in mem:
#                 return mem[(prev, pos)]

#             if pos >= n:
#                 return 0

#             if Parr[pos].a <= prev:
#                 ans = helper(prev, pos+1)

#             else:
#                 ans = max(helper(Parr[pos].b, 0) + 1, helper(prev, pos + 1))

#             mem[(prev, pos)] = ans

#             return ans

#         return helper(0, 0)

## approach 2

#User function Template for python3

'''
class Pair(object):
    def __init__(self, a, b):
        self.a = a
        self.b = b
'''
class Solution:
    def maxChainLen(self,Parr, n):
        # Parr:  list of pair
        #code here

        Parr.sort(key=lambda x: x.b)

        prev = -float('inf')
        ans = 0

        for i in range(n):
            if Parr[i].a > prev:
                prev = Parr[i].b
                ans += 1

        return ans
