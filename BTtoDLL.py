#User function Template for python3

class Node:
    """ Class Node """
    def __init__(self, value):
        self.left = None
        self.data = value
        self.right = None

#Function to convert a binary tree to doubly linked list.
class Solution:
    def bToDLL(self,root):
        # do Code here
        
        if root is None:
            return None
            
        res1 = self.bToDLL(root.left)
        res2 = self.bToDLL(root.right)

        # print(res1)
        # print(res2)
        
        root.right = res2
        if res2 is not None:
            # print(f"res2 data: {res2.data}")
            res2.left = root
        
        if res1 is not None:
            # print(f"res1 data: {res1.data}")
            temp = res1
            while temp.right is not None:
                temp = temp.right
            temp.right = root
            root.left = temp
            return res1
        else:
            root.left = res1
            return root

if __name__ == "__main__":
    root = Node(1)
    root.left = Node(3)
    root.right = Node(2)

    # print(root.data)
    # print(root.left.data)
    # print(root.right.data)

    root = Solution().bToDLL(root)

    print(root.data)
    print(root.left)
    print(root.right.data)
    print(root.right.right.data)