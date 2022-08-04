class Solution():
    def isCompleteBT(self, root):
        #Add Code Here
        
        if not root:
            return True
            
        queue = []
        flag = False
        
        queue.append(root)
        while len(queue) > 0:
            temp = queue.pop(0)
            
            if temp.left:
                if flag == True:
                    return False
                    
                queue.append(temp.left)
                
            else:
                flag = True
                
            if temp.right:
                if flag == True:
                    return False
                    
                queue.append(temp.right)
                
            else:
                flag = True
                
        return True


class Node:
    def __init__(self, val):
        self.right = None
        self.data = val
        self.left = None
""" 
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.right = Node(6)
  
if (Solution().isCompleteBT(root)):
    print ("Complete Binary Tree")
else:
    print ("NOT Complete Binary Tree") """