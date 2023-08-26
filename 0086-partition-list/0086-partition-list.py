# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        dummy_small=ListNode()
        dummy_large=ListNode()

        smallptr=dummy_small
        largeptr=dummy_large

        curr=head

        while curr:
            if curr.val <x:
                smallptr.next=curr
                smallptr=smallptr.next
            else:
                largeptr.next=curr
                largeptr=largeptr.next
            curr=curr.next

        smallptr.next=dummy_large.next
        largeptr.next = None

        return dummy_small.next