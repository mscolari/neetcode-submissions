class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class MyLinkedList:

    def __init__(self):
        self.head = None
        self.length = 0
        
    def get(self, index: int) -> int:
        if index < 0 or index >= self.length:
            return -1
    
        count = 0
        curr = self.head
        while count < index:
            curr = curr.next
            count += 1

        return curr.val
        

    def addAtHead(self, val: int) -> None:
        self.addAtIndex(0, val)

    def addAtTail(self, val: int) -> None:
        self.addAtIndex(self.length, val)

    def addAtIndex(self, index: int, val: int) -> None:
        if index < 0 or index > self.length:
            return

        count = 0
        curr = self.head
        prev = None
        while count < index:
            prev = curr
            curr = curr.next
            count += 1

        new_node = ListNode(val, curr)
        if index == 0:
            self.head = new_node
        else:
            prev.next = new_node
        self.length += 1

    def deleteAtIndex(self, index: int) -> None:
        if index < 0 or index >= self.length:
            return

        count = 0
        curr = self.head
        prev = None
        while count < index:
            prev = curr
            curr = curr.next
            count += 1

        # delete the node
        if index == 0:
            self.head = curr.next
        else:
            prev.next = curr.next
        self.length -= 1

