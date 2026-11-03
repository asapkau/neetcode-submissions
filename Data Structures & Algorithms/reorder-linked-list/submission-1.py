# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow = head
        fast = head.next

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        prev = None
        second = slow.next
        slow.next = prev
        current = second

        while current:
            nextNode = current.next
            current.next = prev
            prev = current
            current = nextNode

        first = head
        second = prev

        while second:
            firstNext = first.next
            first.next = second
            secondNext = second.next
            second.next = firstNext

            first = firstNext
            second = secondNext
        

        