#User function Template for python3
'''
class Node:
    def __init__(self, val):
        self.right = None
        self.data = val
        self.left = None
'''
class Solution:
    # your task is to complete this function
    # function should delete all the Nodes greater than or equal to k
    # function should return the new head to pointer
    def deleteNode(self, root, k):
        # Code here
        if root is None:
            return root
        
        if root.data >= k:
            root = self.deleteNode(root.left, k)
        
        else:
            root.right = self.deleteNode(root.right, k)
            
        return root
