# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        current_node1 = l1
        list1 = []
        while current_node1:
            list1.append(current_node1.val)
            current_node1 = current_node1.next
        
        list1.reverse()
        current_node2 = l2
        list2 = []
        while current_node2:
            list2.append(current_node2.val)
            current_node2 = current_node2.next
        list2.reverse()
        
        res1 = 0
        for i in list1:
            res1 = res1 * 10 + i
            
        res2 = 0
        for i in list2:
            res2 = res2 * 10 + i
        
        res = res1 + res2
        res = str(res)
        res = res[::-1]
        list = []
        for i in range(len(res)):
            list.append(int(res[i]))
        cur = dummy = ListNode(0)
        for e in list:
            cur.next = ListNode(e)
            cur = cur.next
        return dummy.next
                
                
            
