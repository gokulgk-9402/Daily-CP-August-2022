#User function Template for python3

'''
# Node Class:
class Node:
    def __init__(self,val):
        self.data = val
        self.left = None
        self.right = None
'''
class Solution:
    def toSumTree(self, root) :
        #code here
        
        def helper(root):
            if not root:
                return 0
            temp = root.data
            root.data = helper(root.right) + helper(root.left)
            return root.data + temp
             
        return helper(root)