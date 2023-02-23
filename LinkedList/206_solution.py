# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return head
        current_node = head
        val_list = [current_node.val]
        while current_node.next is not None:
            val_list.append(current_node.next.val)
            current_node = current_node.next
        result_node = head
        for i in val_list[::-1]:
            result_node.val = i
            result_node = result_node.next
        return head

                
