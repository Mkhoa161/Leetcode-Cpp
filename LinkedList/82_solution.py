# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        
        curr = head
        dummy = prev = ListNode(0, head)
        run = False
        while curr:
            while curr.next and curr.val == curr.next.val:
                curr = curr.next
                run = True
            
            if run:
                prev.next = curr.next
                curr = curr.next
                run = False
                continue

            prev = prev.next
            curr = curr.next

        return dummy.next


