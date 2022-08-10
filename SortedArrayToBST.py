# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        
        
        def helper(arr):
            if arr == []:
                return None
            
            l = len(arr)
            
            root = TreeNode(arr[l//2])
            root.left = helper(arr[:l//2])
            root.right = helper(arr[l//2+1:])
            
            return root
        
        return helper(nums)