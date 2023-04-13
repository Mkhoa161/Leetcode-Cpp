# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        if not head or not head.next:
            return
        
        # find middle
        fast = slow = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        # reverse the second half
        prev, slow.next, slow = None, None, slow.next # prev = None, slow = 4 -> None
        while slow:
            prev, prev.next, slow = slow, prev, slow.next # prev = 4 -> None, slow = None

        slow = head
        while prev:
            slow.next, slow = prev, slow.next # slow = 1 -> 4 -> None, slow = 2 -> 3 -> None
            prev.next, prev = slow, prev.next # prev = 4 -> 2 -> 3 -> None, prev = None
            
        
        