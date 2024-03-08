# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        dummy = ListNode()
        dummy.next = head

        left_prev = dummy
        curr = head

        index = 1

        while curr and index < left:
            left_prev = curr
            curr = curr.next
            index += 1
        
        prev = None
        tail = curr

        while curr and index <= right:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
            index += 1

        left_prev.next = prev
        tail.next = curr
        
        return dummy.next
