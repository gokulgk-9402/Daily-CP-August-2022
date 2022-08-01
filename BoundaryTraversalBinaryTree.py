#User function Template for python3

'''
class Node:
    def __init__(self, val):
        self.right = None
        self.data = val
        self.left = None
'''
class Solution:
    def printBoundaryView(self, root):
        # Code here
        ans = []
            
        def leftboundary(node):
            if node == None:
                return 
            
            if node.left:
                ans.append(node.data)
                leftboundary(node.left)
                
            elif node.right:
                ans.append(node.data)
                leftboundary(node.right)
                
        def leaves(node):
            if node == None:
                return
            
            leaves(node.left)
            if node.left == None and node.right == None:
                ans.append(node.data)
                
            leaves(node.right)
                
        def rightboundary(node):
            if node == None:
                return
            
            if node.right:
                rightboundary(node.right)
                ans.append(node.data)
                
            elif node.left:
                rightboundary(node.left)
                ans.append(node.data)
        
        ans.append(root.data)
        leftboundary(root.left)
        leaves(root.left)
        leaves(root.right)
        rightboundary(root.right)
        
        return ans
            