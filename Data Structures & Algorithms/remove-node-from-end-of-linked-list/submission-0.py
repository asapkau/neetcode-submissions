# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:

        length = 0
        current = head

        while current:
            current = current.next
            length += 1
        
        nodeToRemove = length - n
        currNode = 0

        nodeAt = head

        while currNode < nodeToRemove - 1:
            nodeAt = nodeAt.next
            currNode += 1

        if nodeToRemove == 0:
            return head.next
        nodeAt.next = nodeAt.next.next
        return head

            
            

        
        