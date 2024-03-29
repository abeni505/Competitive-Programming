class Node:
    def __init__(self,val):
        self.val = val
        self.next = None
class MyLinkedList:

    def __init__(self):
        self.head = None
        
    def get(self, index: int) -> int:
        
        curr = self.head
        for i in range(index):
            if curr:
                curr = curr.next
       
        if curr:
            return curr.val
        else:
            return -1

    def addAtHead(self, val: int) -> None:
        new_node = Node(val)
        new_node.next = self.head
        self.head = new_node
        

    def addAtTail(self, val: int) -> None:

        new_node = Node(val)
        if not self.head:
            self.head = new_node

        curr = self.head
        while curr.next:
            curr = curr.next
        curr.next = new_node
        new_node.next = None
       
        
    def addAtIndex(self, index: int, val: int) -> None:
        if index == 0:
            self.addAtHead(val)
            return

        new_node = Node(val)
    
        curr = self.head
        for i in range(index - 1):
            if curr:
                curr = curr.next
          
        if curr:
            temp = curr.next
            curr.next = new_node
            new_node.next = temp
    

    def deleteAtIndex(self, index: int) -> None:
        if index == 0 and self.head:
            self.head = self.head.next
        
        curr = self.head
        for i in range(index - 1):
            if curr:
                curr = curr.next

        if curr and curr.next:
            curr.next = curr.next.next
        


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)