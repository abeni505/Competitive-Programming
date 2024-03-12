# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeZeroSumSublists(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        curr = dummy
        run_sum = 0
        hashmap = {0: dummy}

      
        while curr is not None:
            run_sum += curr.val
            hashmap[run_sum] = curr
            curr = curr.next

       
        run_sum = 0
        curr = dummy

        while curr is not None:
            run_sum += curr.val
            curr.next = hashmap[run_sum].next
            curr = curr.next

        return dummy.next