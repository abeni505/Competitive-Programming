# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy_odd=ListNode()
        dummy_even=ListNode()

        oddptr=dummy_odd
        evenptr=dummy_even

        curr=head

        evenflag = True
        while curr:
            if evenflag:
                evenptr.next=curr
                evenptr=evenptr.next
                
            else:
                oddptr.next=curr
                oddptr=oddptr.next
                
            curr=curr.next
            evenflag= not evenflag

        evenptr.next=dummy_odd.next
        oddptr.next=None

        return dummy_even.next