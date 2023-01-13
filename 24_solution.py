# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        prev, curr = dummy, head

        while curr and curr.next:
            # Store needed node
            next_pair = curr.next.next
            second_node = curr.next
            
            # Swapping
            second_node.next = curr
            curr.next = next_pair
            prev.next = second_node 

            # Updating
            prev = curr
            curr = curr.next
        return dummy.next
            
