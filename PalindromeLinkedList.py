# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        arr = []
        temp = head
        length = 0
        
        while temp!=None:
            arr.append(temp.val)
            temp = temp.next
            length += 1
            
        i = 0
        while i < length//2:
            if arr[i] != arr[length - i - 1]:
                return False
            i += 1
            
        return True