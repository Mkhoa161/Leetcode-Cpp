# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        curr_node = head
        prev_node = None
        if head is None:
            return head
        while curr_node is not None:
            if prev_node and curr_node.next is None and curr_node.val == val:
                prev_node.next = None
            elif prev_node and curr_node.next and curr_node.val == val:
                prev_node.next = curr_node.next
                curr_node = curr_node.next
                continue
            elif not prev_node and head.val == val:
                curr_node = curr_node.next
                head = head.next
                prev_node = None
                continue
            prev_node = curr_node
            curr_node = curr_node.next
        return head
