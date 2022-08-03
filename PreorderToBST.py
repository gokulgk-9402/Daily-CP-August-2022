
class Node:

    def __init__(self, data=0):
        self.data = data
        self.left = None
        self.right = None

#Function that constructs BST from its preorder traversal.

def post_order(pre, size) -> Node:
    #code here
    inorder_list = pre[:]
    inorder_list.sort()
    
    def bs(arr, ele):
        left = 0
        right = len(arr) - 1

        while left <= right:
            mid = (left + right)//2
            if arr[mid] == ele:
                return mid

            elif arr[mid] < ele:
                left = mid + 1

            else:
                right = mid - 1
        
        return -1
    
    def helper(preorder, inorder):
        if len(preorder) == 0:
            return None

        root = Node(preorder[0])
        pos = bs(inorder, preorder[0])
        root.left = helper(preorder[1:pos+1], inorder[:pos])
        root.right = helper(preorder[pos+1:], inorder[pos+1:])

        return root

    return helper(pre, inorder_list)


print(post_order([40,30,35,80,100], 5).left.data)