class ListNode:
    def __init__(self, val, next = None):
        self.val = val
        self.next = next

class MyLinkedList:

    def __init__(self, head = None):
        self.head = head
        self.size = 0         

    def get(self, index: int) -> int:
        if index < 0 or index > self.size - 1:
            return -1
        temp = self.head
        for i in range(index):
            temp = temp.next
        return temp.val


    def addAtHead(self, val: int) -> None:
        new_node = ListNode(val, self.head)
        self.head = new_node
        self.size += 1

    def addAtTail(self, val: int) -> None:
        if self.head is None:
            self.head = ListNode(val)
            self.size += 1
            return
        curr_node = self.head
        while curr_node.next is not None:
            curr_node = curr_node.next
        curr_node.next = ListNode(val)
        self.size += 1
        

    def addAtIndex(self, index: int, val: int) -> None:
        if index > self.size:
            return
        prev_node = None
        curr_node = self.head
        track = 0
        if index <= 0:
            new_node = ListNode(val, self.head)
            self.head = new_node
            self.size += 1
            return

        if index == self.size:
            while curr_node.next is not None:
                curr_node = curr_node.next
            curr_node.next = ListNode(val)
            self.size += 1
            return

        while curr_node is not None:
            if index == track:
                new_node = ListNode(val)
                new_node.next = curr_node
                prev_node.next = new_node
                self.size += 1
                return
            track += 1
            prev_node = curr_node
            curr_node = curr_node.next

    def deleteAtIndex(self, index: int) -> None:
        if index < 0 or index > self.size - 1:
            return
        curr_node = self.head
        prev_node = None
        track = 0
        if index == 0:
            self.head = self.head.next
            self.size -= 1
            return
        while curr_node is not None:
            if index == track:
                prev_node.next = curr_node.next
                self.size -= 1
                return
            else:
                prev_node = curr_node
                curr_node = curr_node.next
                track += 1
