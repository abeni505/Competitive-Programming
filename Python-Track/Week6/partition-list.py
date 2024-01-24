# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        
        dummy = ListNode()
        dummy2 = ListNode()


        left = dummy
        right = dummy2

        curr = head
        while curr:
            if curr.val < x:
                left.next = curr
                left = left.next

            else:
                right.next = curr
                right = right.next

            curr = curr.next

        left.next = dummy2.next
        right.next = None


        return dummy.next
       