# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        if not head:
            return head

        while head and head.val == val:
            head = head.next
        
        prev = None
        curr = head

        while curr:
            if curr.val == val:
                if curr.next is not None:
                    prev.next = curr.next
                    curr.next = None
                    curr = prev.next
                    continue
                else:
                    prev.next = None
            
            prev = curr
            curr = curr.next
        
        return head
            
