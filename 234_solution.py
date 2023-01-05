# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        if head is None:
            return False
        curr_node = head
        val_list = [curr_node.val]
        while curr_node.next is not None:
            val_list.append(curr_node.next.val)
            curr_node = curr_node.next
        for index in range(len(val_list)):
            if val_list[index] != val_list[len(val_list)-1-index]:
                return False
        return True

