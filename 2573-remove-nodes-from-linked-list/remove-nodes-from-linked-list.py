class Solution:
    def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        prev, curr = None, head
        while curr:
            curr.next, prev, curr = prev, curr, curr.next

      
        dummy = ListNode()
        temp, curr = dummy, prev
       
        while curr:
            if curr.val >= temp.val:
                temp.next = curr
                temp = curr
                curr = curr.next
            else:
                curr = curr.next

        temp.next = None
        
        new_prev = None
        curr = dummy.next
        while curr:
            curr.next, new_prev, curr = new_prev, curr, curr.next

        return new_prev