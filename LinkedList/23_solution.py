# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        lst = []
        for head in lists:
            curr = head
            while curr is not None:
                lst.append(curr.val)
                curr = curr.next
        lst.sort()
        head = curr = ListNode(0)
        for value in lst:
            curr.next = ListNode(value) 
            curr = curr.next
        return head.next
