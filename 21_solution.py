# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        list_1 = []
        current1 = list1
        while current1:
            list_1.append(current1.val)
            current1 = current1.next
        
        list_2 = []
        current2 = list2
        while current2:
            list_2.append(current2.val)
            current2 = current2.next
        
        list = list_1 + list_2
        list.sort()
        curr = temp = ListNode(0)
        for i in list:
            curr.next = ListNode(i)
            curr = curr.next
        return temp.next
