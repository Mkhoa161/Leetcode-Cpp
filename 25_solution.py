# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        slow = fast = head
        stack = []
        while fast:
            stack.append(fast.val)
            if len(stack) == k:
                while stack:
                    slow.val = stack.pop()
                    slow = slow.next
            fast = fast.next
        return head
